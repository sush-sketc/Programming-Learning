# Our store's single machine three node test group replication

部署组复制的最常见方法是使用多个节点机器进行部署，但是本次作为测试学习目录，在一台上面使用初始化三个实例进行测试。
> [!WARNING]
> 组复制通常部署在多个主机上，因为它可以确保高可用性。 本节中的说明不适用于生产部署，因为所有 MySQL 服务器实例都在同一台主机上运行。 如果该主机发生故障，则整个组都会发生故障。 因此，此信息应用于测试目的，而不是生产环境。

# Node Description
创建包含三个 MySQL Server 实例的复制组。 这意味着您需要三个数据目录（每个服务器实例一个），并且必须单独配置每个实例。 该目录mysql-8.0位于名为的目录中- 此过程假定您已下载并解压 MySQL Server 。 每个 MySQL 服务器实例都需要一个特定的数据目录。data创建一个名为的目录，并在该目录中为每个服务器实例（例如 s1、s2 和 s3）创建子目录并初始化每个子目录。
可以参考本部署操作文档[Rocky Linux9.5 (Source Installation Methods).md](../Install/Rocky%20Linux9.5%20(Source%20Installation%20Methods).md),

<table>
    <tr>
        <th>实例PATH</th>
        <th>MySQL 版本</th>
        <th>插件版本</th>
    </tr>
    <tr>
        <td>/mnt/mysql/33061</td>
        <td rowspan=4 align="center">8.0.40 </td>
        <td rowspan=4 align="center">组复制是 MySQL Server 8.0 提供的内置 MySQL 插件，因此无需额外安装</td>
    </tr>
    <tr>
        <td>/mnt/mysql/33062</td>
    </tr>
     <tr>
        <td>/mnt/mysql/33063</td>
    </tr>
</table>

# 存储引擎

对于组复制，数据必须存储在 `InnoDB` 事务存储引擎中（有关详细信息，请参见第 18.9.1 节“组复制的要求” ）。 使用其他存储引擎（包括临时MEMORY存储引擎）可能会导致组复制出现错误。`disabled_storage_engines`通过如下设置系统变量来避免使用它：
```sh
disabled_storage_engines="MyISAM,BLACKHOLE,FEDERATED,ARCHIVE,MEMORY"
```
`MyISAM`如果存储引擎被禁用，将 MySQL 实例升级到仍然使用`mysql_upgrade`的版本（MySQL 8.0.16 之前的版本）可能会导致`mysql_upgrade`失败并出现错误。 为了解决这个问题，请在运行`mysql_upgrade`时重新启用该存储引擎，并在服务器重新启动时再次禁用它。 有关更多信息，请参见 第 4.4.5 节“mysql_upgrade - 检查和升级 MySQL 表” 。

# 复制框架
以下设置根据 MySQL 组复制要求配置复制。

```plain
server_id=1
gtid_mode=ON
enforce_gtid_consistency=ON
```
这些设置使用唯一标识符编号 1启用[使用全局事务标识符进行复制”](../MySQLGroupReplication/Requirements%20and%20limitations.md)，并将服务器配置为仅执行可以使用 GTID 安全记录的语句。

#如果版本>MySQL 8.0.20，您还需要设置：
```plain
binlog_checksum=NONE
```
此设置禁用写入二进制日志的事件的校验和，默认情况下启用。从 MySQL 8.0.21 开始，组复制支持在二进制日志中存在校验和，并可以使用它们来验证某些通道上事件的完整性，因此可以使用默认设置。 有关更多信息，请参见[组复制要求”](../MySQLGroupReplication/Requirements%20and%20limitations.md)
如果您使用的 MySQL 8.0.3 之前的版本（该版本具有改进的复制默认值），您还需要将以下行添加到成员选项文件中： 如果您的更高版本选项文件包含这些系统变量，请确保它们设置如下：
```plain
log_bin=binlog
log_slave_updates=ON
binlog_format=ROW
master_info_repository=TABLE
relay_log_info_repository=TABLE
transaction_write_set_extraction=XXHASH64
```

# 组复制设置

此时，选项文件配置服务器，指示其在特定配置中实例化复制基础结构。 在下一部分中，您将为服务器配置组复制设置。
```plain
plugin_load_add='group_replication.so'
group_replication_group_name="aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa"
group_replication_start_on_boot=off
group_replication_local_address= "s1:33061"
group_replication_group_seeds= "s1:33061,s2:33061,s3:33061"
group_replication_bootstrap_group=off
```
<table width: 100%;table-layout: auto;>
    <tr>
        <th><font style="font-size: 120%;color:purple">名称</font></th>
        <th><font style="font-size: 120%;color:purple">描述</font></th>
    </tr>
    <tr>
        <td><pre><code style="color:Orange">plugin-load-add</code></pre></td> 
        <td border: 12px solid #000;padding: 10px;>将组复制插件添加到服务器启动时加载的插件列表中。 对于生产部署，建议这样做，而不是手动安装插件</td>
    </tr>
    <tr>
        <td><pre><code style="color: Orange">group_replication_group_name</code></pre></td>
        <td>这个配置告诉插件你要加入或创建的组的名称是“aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaa”</td>
    </tr>
    <tr>
        <td><pre><code style="color: Orange">group_replication_group_name</code></pre></td>
        <td>该值必须是有效的 UUID。 在二进制日志中设置组复制事件的 GTID 时，此 UUID 在内部使用。SELECT UUID()您可以使用以下方式生成 UUID</td>
    </tr>
   <tr>
        <td><pre><code style="color: Orange">group_replication_start_on_boot</code></pre></td>
        <td>指示插件不要在服务器启动时自动启动操作。 在设置组复制时这一点很重要，以便您可以在手动启动插件之前配置服务器。 
        配置成员后，您可以设  置为 group_replication_start_on_boot  在服务器启动时自动启动组复制。on </td>
    </tr>
    <tr>
        <td><pre><code style="color: Orange">group_replication_local_address</code></pre></td> 
        <td>
            <p>配置设置成员用于与组中其他成员进行内部通信的网络地址和端口。 组复制使用此地址进行内部成员到成员的连接，包括到组通信引擎（XCom，一种 Paxos 变体）的远程实例。</p>
            <p>group_replication_local_address` 配置的网络地址必须能够被所有组成员解析。 例如，如果每个服务器实例都在具有固定网络地址的不同机器上，则可以使用机器的 IP 地址，例如 10.0.0.1。</p> 
            <p>如果使用主机名，`/etc/hosts`则必须使用完全限定名称，并确保它可以通过 DNS、正确配置的文件或其他名称解析过程进行解析。</p>
            <p>从 MySQL 8.0.14 开始，您可以将 IPv6 地址（或解析为它们的主机名）与 IPv4 地址一起使用。 </p>
            <p>一个群组可以混合拥有使用 IPv6 的成员和使用 IPv4 的成员.</p>
            <p>group_replication_local_address`建议端口为33061。`group_replication_local_address`由组复制用作复制组内组成员的唯一标识符。 </p>
            <p>如本教程所示，您可以对复制组的所有成员使用相同的端口，只要主机名或 IP 地址都不同。 或者，您可以对所有成员使用相同的主机名或 IP 地址，只要端口都不同</p>
        </td>
    </tr>
    <tr>
        <td><pre><code style="color: Orange">group_replication_group_seeds</code></pre></td>
        <td>配置设置组成员的主机名和端口，新成员将使用它们与组建立连接。 这些成员被称为种子成员。 建立连接后，组成员信息replication_group_members将列在性能模式表中。 通常，        group_replication_group_seeds列表包括group_replication_local_address每个组成员hostname:port，但这不是强制性的，您可以选择组成员的子集作为种子。</td>
    </tr>
    <tr>
        <td><pre><code style="color: Orange">group_replication_bootstrap_group</code></pre></td> 
        <td>
            配置告诉插件是否引导组。 在这种情况下，您可以在选项文件中将此变量设置为 off，即使 s1 是该组的第一个成员。 
            相反，group_replication_bootstrap_group在实例运行时对其进行配置，以确保只有一个成员实际引导该组。</td>
    </tr>
</table>


组复制分布式恢复过程中，现有成员向加入成员提供的连接`group_replication_local_address`不是由直到 MySQL 8.0.20，组成员提供标准 SQL 客户端连接，用于加入成员以进行由MySQL 服务器hostname和系统变量指定的分布式恢复。port从 MySQL 8.0.21 开始，组成员可以将分布式恢复端点的备用列表公布为专用于成员参与的客户端连接。 有关更多信息，请参见 第 18.4.3.1 节“分布式恢复连接” 。
> [!IMPORTANT]
> 组复制本地地址必须与 MySQL 服务器`hostname`和系统变量`port`中定义的用于 SQL 客户端连接的主机名和端口不同。 请勿将其用于客户端应用程序。 它仅应在组复制运行时用于组成员之间的内部通信。
> 如果加入的成员无法使用 MySQL 服务器系统变量中定义的主机名正确识别其他成员，`hostname`则分布式恢复可能会失败。建议通过 `DNS` 或本地设置正确配置运行 MySQL 的操作系统的唯一主机名。 您可以通过性能模式表`replication_group_members`中的列`Member_host`查看服务器用于SQL 客户端连接的主机名： 如果多个组成员外部化操作系统设置的默认主机名，则加入的成员可能无法解析到正确的成员地址，并且无法连接进行分布式恢复。 在这种情况下，`report_host`您可以使用 MySQL 服务器系统变量来配置每个服务器将外部化的唯一主机名。
> `group_replication_group_seeds`列出的地址是 配置的种子成员的内部网络地址，而不是性能模式`hostname:port`表等中所示的用于 SQL 客户端连接的地址。 `group_replication_local_addressreplication_group_membershostname:port`

启动组的服务器不使用此选项。这是因为此选项是初始服务器，负责引导组。 这意味着引导该组的服务器上的现有数据将用作下一个加入成员的数据。当第二台服务器加入时，它会被要求加入组中唯一的成员，第二台服务器上的缺失数据会从引导成员上的捐赠者数据中复制，然后该组就会扩大。可以请求第三个服务器绑定来绑定这两者中的任何一个。数据已同步至新成员，群组再次扩大。 后续服务器加入时会重复此过程。

> [!WARNING]
> 如果您同时加入多个服务器，请确保指向组中已有的种子成员。 已加入小组的成员不应作为种子，因为在联系时他们可能还不是小组的一部分。
> 建议您先启动引导成员，再创建组。 然后让他们成为其余参与成员的种子成员。 当你加入剩余成员时，这将形成一个小组。
> 不支持创建群组并让多个成员同时加入。 这可能会有效，但操作可能会发生冲突，然后加入组操作将以错误或超时结束。

加入成员`group_replication_group_seeds`必须使用种子成员可选宣传的相同协议（IPv4 或 IPv6）与种子成员进行通信。 为了实现组复制 IP 地址授权，种子成员的允许列表必须包含种子成员所服务的协议的参与成员的 IP 地址，或解析为这些协议地址的主机名。 如果该地址的协议与通告给种子成员的协议不匹配，`group_replication_local_address`则除了加入成员之外，还必须配置并允许该地址或主机名。 如果加入成员没有相应协议的允许地址，则连接尝试将被拒绝.

> [!IMPORTANT]
> `group_replication_bootstrap_group`该变量必须仅对属于该组的一个服务器实例可用。这通常是在您第一次引导一个组时完成的（或者当您停止并重新启动整个组时）。 如果多次引导一个组（例如，如果多个服务器实例设置了此选项），则可以创建一个人工裂脑场景，其中有两个具有相同名称的不同组。 请确保在第一个服务器实例上线后`group_replication_bootstrap_group=off`进行设置 。

# Comprehensive configuration

<details>
<summary><font style="font-size: 110%;color: bisque">Based on instance 33061 configuration</font> </summary>

编辑`/mnt/mysql/33061/config/server.cnf`文件添加
> [!WARNING]
> 当前是我本地测试路径，如需修改按照自己实际环境进行修改，当前仅为，测试，验证，学习，不可用于实际环境

```sh
########################## Basic Configure ##########################
server_id=xxx
gtid_mode=ON                      //启用GTID
enforce_gtid_consistency=ON       //强制GTID的一致性
master_info_repository=TABLE      //将master.info元数据保存在系统表中
relay_log_info_repository=TABLE   //将relay.info元数据保存在系统表中
log_bin=binlog                    //开启二进制日志记录
binlog_format=ROW                 //以行的格式记录
log_slave_updates=ON              //级联复制
binlog_checksum=NONE              //禁用二进制日志事件校验
########################## MGR Configure ##############################
transaction_write_set_extraction=XXHASH64
loose-group_replication_group_name="aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa"
loose-group_replication_start_on_boot=off
loose-group_replication_local_address= "192.168.66.xxx:3406"
loose-group_replication_group_seeds= "192.168.66.150:3406,192.168.66.151:3406,192.168.66.152:3406"
loose-group_replication_bootstrap_group=off
loose-group_replication_member_weight=50
loose-group_replication_single_primary_mode=TRUE  # 是否启动单主模式
loose-group_replication_enforce_update_everywhere_checks=FALSE  # 是否启动多主模式
```

<details>
<summary><font style="font-size: 110%;color: bisque">Parameter Description</font> </summary>


<table width: 100%;table-layout: auto;>
    <tr>
        <th><font style="font-size: 120%;color:purple">名称</font></th>
        <th><font style="font-size: 120%;color:purple">说明</font></th>
    </tr>
    <tr>
        <td> <code style="font-size: 105%;color: Orange">server_id </code></td>
        <td >
            <p style="text-align:left"> 此变量指定服务器 ID。 server_id默认设置为 1。可以使用此默认 ID 启动服务器，但启用二进制日志记录时，如果您未server_id明确设置以指定服务器 ID，则会发出一条信息性消息。</p>
            <p style="text-align:left">对于复制拓扑中使用的服务器，必须为每个复制服务器指定唯一的服务器 ID，范围从 1 到 2 32 − 1。 “唯一”表示每个 ID 必须与复制拓扑中任何其他源或副本使用的每个其他 ID 不同。</p>
            <p style="text-align:left">如果服务器 ID 设置为 0，则会进行二进制日志记录，但服务器 ID 为 0 的源会拒绝来自副本的任何连接，而服务器 ID 为 0 的副本会拒绝连接到源。</p>
            <p style="text-align:left">请注意，虽然您可以动态地将服务器 ID 更改为非零值，但这样做并不能立即启动复制。您必须更改服务器 ID，然后重新启动服务器以初始化副本</p>
        </ul>
        </td></tr>
    <tr>
        <td><code style="font-size: 105%;color: Orange">gtid_mode</code></td>
        <td>
            <p style="text-align:left">控制是否启用基于 GTID 的日志记录以及日志可以包含哪些类型的事务。您必须具有足够的权限才能设置全局系统变量。请参见 第 7.1.9.1 节“系统变量权限”。</p>
            <p style="text-align:left">enforce_gtid_consistency必须先设置为，ON然后才能设置 gtid_mode=ON。在修改此变量之前，请参见 第 19.1.4 节“更改在线服务器上的 GTID 模式”。</p>
            <p style="text-align:left">记录的事务可以是匿名的，也可以使用 GTID。匿名事务依靠二进制日志文件和位置来识别特定事务。GTID 事务具有用于引用事务的唯一标识符。不同的模式如下：</p>
                <ul>
                    <li><code style="color: Orange">OFF</code>：新的和复制的交易都必须是匿名的。</li>
                    <li><code style="color: Orange">OFF_PERMISSIVE</code>：新事务是匿名的。复制的事务可以是匿名事务，也可以是 GTID 事务。</li>
                    <li><code style="color: Orange">ON_PERMISSIVE</code>：新事务是 GTID 事务。复制事务可以是匿名事务，也可以是 GTID 事务。</li>
                    <li><code style="color: Orange">ON</code>：新建事务和复制事务都必须是 GTID 事务。</li>
                </ul>
            <p style="text-align:left">从一个值到另一个值的更改只能一步一步进行。例如，如果 gtid_mode当前设置为 OFF_PERMISSIVE，则可以更改为 OFF或 ，ON_PERMISSIVE但不能更改为ON。</p>
            <p style="text-align:left">无论的值如何gtid_purged， 和 gtid_executed的值都是不变的 gtid_mode。因此，即使在 的值发生变化后 gtid_mode，这些变量仍包含正确的值。</p>
        </td> </tr>
    <tr>
        <td><code style="font-size: 105%;color: Orange">enforce_gtid_consistency</code></td>
        <td>
        <p>根据此变量的值，服务器通过仅允许执行可以使用 GTID 安全记录的语句来强制执行 GTID 一致性。您 必须ON在启用基于 GTID 的复制之前 设置此变量 。</p>
        <p>可配置的值 enforce_gtid_consistency有：</p>
        <ul>
            <li><code style="color: Orange">OFF</code>：允许所有事务违反GTID一致性。</li>
            <li><code style="color: Orange">ON</code>：不允许任何事务违反GTID一致性。</li>
            <li><code style="color: Orange">WARN</code>：允许所有事务违反 GTID 一致性，但是这种情况下会发出警告。</li>
        </ul>
        <p>--enforce-gtid-consistency仅当对语句进行二进制日志记录时才会生效。如果服务器上禁用了二进制日志记录，或者语句因被过滤器删除而未写入二进制日志，则不会对未记录的语句检查或强制执行 GTID 一致性。</p>
        <p>enforce_gtid_consistency当设置为时， 只有使用 GTID 安全语句可以记录的语句才会被记录 ON，因此这里列出的操作不能与此选项一起使用：</p>
        <ul>
            <li>CREATE TEMPORARY TABLE或 DROP TEMPORARY TABLE交易内部的语句。  </li>
            <li>同时更新事务和非事务表的事务或语句。有一个例外，即如果所有 非事务表都是临时的，则允许在同一事务中或与事务 DML 在同一语句中使用非事务 DML。</li>
            <li>CREATE TABLE ... SELECTMySQL 8.0.21 之前版本支持语句。从 MySQL 8.0.21 开始， CREATE TABLE ... SELECT支持原子 DDL 的存储引擎允许使用语句。</li>
        </ul></td>
    </tr>
</table>



</details></details>

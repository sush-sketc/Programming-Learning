
## Rocky9 源码编译安装MMySQL8
<font style="background:#F6E1AC;color:#664900">rocky-linux</font>      <font style="background:#DBF1B7;color:#2A4200">MySQL8.0</font>

### 1. 系统信息
```plantuml
ARCH:  			5.14.0-503.19.1.el9_5.aarch64

CPU-INFO:		processor : 4

FREE-INFO:		8G
```

### 2. 系统配置
> `pam_limits.os`模块将`ulimit`限制，`nice`优先级和同时登陆回会数限制应用于用户登陆会话，此配置文件为`limits.conf`- `pam_limits`模块的配置文件

```sh

if [ $(cat /etc/security/limits.conf |grep "mysql" |wc -l) -lt 1 ];then sudo tee -a /etc/security/limits.conf > /dev/null <<"ROF"
* soft nproc 65536
* hard nproc 65536
* soft nofile 65536
* hard nofile 65536
mysql soft nproc 65536
mysql hard nproc 65536
mysql soft nofile 65536
mysql hard nofile 65536
ROF
fi
```

```sh

if [ -e /etc/security/limits.d/90-nproc.conf ];then \
  if [ $( cat /etc/security/limits.d/90-nproc.conf  | grep "mysql" | wc -l )  -lt 1 ] ;then \
    cat >>/etc/security/limits.d/90-nproc.conf<<EOF
mysql       soft    nproc     unlimited
EOF
  fi
fi
```

+ `CMake`版本建议使用`GUN CMake 3.75`或更高版本，
+ 从`mysql 8.0.26`开始，MySQL8.0源代码允许使用`C++17`功能，最低编译器版本适用`Linux GCC 10`或`Clang 5`
+ `MySQL C API`需要`C++`或`C99`编译器才能编译
+ `SSL`库是支持加密连接，随机数生成嫡和其他加密相关操作所必须的，默认情况下，构建使用主机系统上安装的`OpenSSL`库，但是需要使用参数`WITH_SSL`在调用`CMake`是使用该选项`cmake . -DWITH_SSL=system`。
+ <font style="color:#DF2A3F;">注意</font>⚠️：如果使用系统默认参数，需确保系统上安装了`OpenSSL 1.0.1` 或更新版本库，如果安装的`OpenSSL`版本低于`1.0.1`在`CMake`时会报错，需要获取`OpenSSL` [访问](http://www.openssl.org)官方文档
+ 构建`MySQL`需要`Boost C++`库(但是不能使用它)。`MySQL`编译需要特定的`Boost`版本，但是如果不同版本的`MySQL`需要不用的`Boost`版本，如果版本不对应则在编译检查时报错，并且会显示一条消息，用以指明当前`MySQL`版本所需的`Boost`库版本，`CMake . -DWITH_BOOST=/path/boost_version_number`。
+ `ncurses`库
+ `bison 2.1`或更高版本.
+ <font style="color:#DF2A3F;">注意</font>⚠️：不再支持版本1，尽可能的使用最新版本的`bison`如果如果检查错误，请升级到更高版本，而不是恢复到早期版本.
+ <font style="color:#DF2A3F;">注意</font> ⚠️：本次使用官方自带boost版本进行编译，不需要额外进行配置.
  
所需依赖包`gcc`工具集

```sh
cmake bison openssl openssl-devel ncurses tar gcc-toolset-12-gcc-c++ gcc-toolset-12 wget libtirpc rpcgen
```

### 3. 添加用户

```sh

if [ ! $(id -u "mysql") ]; then echo "mysql user is not exists for to created"; \
/usr/sbin/groupadd mysql && /usr/sbin/useradd -g mysql -r -s /sbin/nologin -M mysql; \
fi
```

> <font style="color:#74B602;">用户mysql拥有MySQL数据目录。它还用于运行mysqld服务器进程，如 systemd mysqld.service文件中所定义（请参阅 </font>[<font style="color:#74B602;">使用 systemd 启动服务器</font>](https://dev.mysql.com/doc/mysql-secure-deployment-guide/5.7/en/secure-deployment-post-install.html#secure-deployment-systemd-startup)<font style="color:#74B602;">）。用户 mysql对 MySQL 数据目录中的任何内容都有读写权限。它不具备登录 MySQL 的能力。它仅出于所有权目的而存在。</font>
>
> <font style="color:#74B602;">如果您的系统还没有用于运行</font><font style="color:#74B602;">[`mysqld`](https://dev.mysql.com/doc/refman/5.7/en/mysqld.html)</font><font style="color:#74B602;">用户和组，您可能需要创建它们。以下命令添加</font> <font style="color:#74B602;">`mysql`</font><font style="color:#74B602;">组和 </font><font style="color:#74B602;">`mysql`</font><font style="color:#74B602;">用户。您可能希望将用户和组命名为 而不是。如果是这样，请按照以下说明替换适当的名称。 useradd和 groupadd</font><font style="color:#74B602;">`mysql`</font><font style="color:#74B602;">的语法在不同版本的 Unix/Linux 上可能略有不同，或者它们可能具有不同的名称，例如 adduser和addgroup</font>
>

## 4. 目录规划 <a name="dir"></a>
```plantuml

basedir             = /mnt/mysql/mysql-executable                  
datadir             = /mnt/mysql/33061/data
binlog              = /mnt/mysql/33061/binlog/mysql-bin
relay               = /mnt/mysql/33061/relay
tmp                 = /mnt/mysql/33061/tmp
mysql.pid           = /mnt/mysql/33061/mysql.pid
mysql.sock          = /mnt/mysql/33061/mysql.sock
innodb_data_home_dir= /mnt/mysql/33061/innodb
config              = /mnt/mysql/3306/config
log-error           = /va/log/mysql/33061-error.log

#创建目录
sudo mkdir -m 0750 -p /mnt/mysql/33061/{mysql-executable,data,binlog,tmp,innodb,config}
sudo mkdir -pv /var/log/mysql/
#目录授权
sudo chown -R mysql:mysql /mnt/mysql/33061 
sudo chown -R mysql:mysql /var/log/mysql/
```

### 5. 安装MySQL <a name="inst"></a>

Cmake选项说明

+ **`-DCMAKE_INSTALL_PREFIX=dir_name`**
    - 安装基目录，可以使用选项在服务器启动时设置此值 --basedir
+ **`-DINSTALL_LAYOUT=name`**
    - 选择预定义的安装布局：`STANDALONE`;`.tar.gz`与和 包使用的布局相同 `.zip`。这是默认设置。`RPM`：与RPM包类似的布局。
+ **`-DMYSQL_DATADIR=dir_name`**
    - MySQL 数据目录的位置。可以使用选项在服务器启动时设置此值 [--datadir](https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html#sysvar_datadir)。
+ **`-DDEFAULT_CHARSET=charset_name`**
    - 服务器字符集。默认情况下，MySQL 使用 `utf8mb4`字符集。
+ **`-DDEFAULT_COLLATION=collation_name`**
    - 服务器排序规则。默认情况下，MySQL 使用 `utf8mb4_0900_ai_ci`。使用 [SHOW COLLATION](https://dev.mysql.com/doc/refman/8.0/en/show-collation.html)语句确定每个字符集可用的排序规则。
    - 可以使用选项在服务器启动时设置此值 [--collation_server](https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html#sysvar_collation_server)。
+ **`-DENABLED_LOCAL_INFILE=bool`**
    - `LOCAL`此选项控制MySQL 客户端库的 内置默认 功能。请参见 [第 8.1.6 节“LOAD DATA LOCAL 的安全注意事项”](https://dev.mysql.com/doc/refman/8.0/en/load-data-local-security.html)。
+ **`-DMYSQL_TCP_PORT=port_num`**
    - 服务器侦听 TCP/IP 连接的端口号。默认值为 3306。可以使用选项在服务器启动时设置此值 [--port](https://dev.mysql.com/doc/refman/8.0/en/server-options.html#option_mysqld_port)。
+ **`-DSYSCONFDIR=dir_name`**
    - 默认`my.cnf`选项文件目录。此位置无法在服务器启动时设置，但您可以使用选项通过给定的选项文件启动服务器 ，其中是文件的完整路径名。 [--defaults-file=file_name](https://dev.mysql.com/doc/refman/8.0/en/option-file-options.html#option_general_defaults-file)`_**file_name**_`
+ **`-DWITH_ARCHIVE_STORAGE_ENGINE=1`**
+ **`-DWITH_BLACKHOLE_STORAGE_ENGINE=1`**
    - 使用InnoDB存储引擎

```sh

wget -q -c  --no-check-certificate https://downloads.mysql.com/archives/get/p/23/file/mysql-boost-8.0.20.tar.gz
#验证下载文件完整性
echo "1f9d75caca32d411eaaf979002253135 mysql-boost-8.0.20.tar.gz"|md5sum -c
#解压预编译
sudo cmake \
-DCMAKE_INSTALL_PREFIX=/mnt/mysql/mysql-executable \
-DINSTALL_LAYOUT=STANDALONE \
-DDEFAULT_CHARSET=utf8mb4 \
-DDEFAULT_COLLATION=utf8mb4_general_ci \
-DENABLED_LOCAL_INFILE=OFF \
-DMYSQL_TCP_PORT=33061 \
-DCOMPILATION_COMMENT='MySQL Server (GPL) Customised Version by ssh(sshrise206516@gmail.com)' \
-DWITH_ARCHIVE_STORAGE_ENGINE=1 \
-DWITH_BLACKHOLE_STORAGE_ENGINE=1 \
-DWITH_PERFSCHEMA_STORAGE_ENGINE=1 \
-DWITH_EXAMPLE_STORAGE_ENGINE=1 \
-DWITH_FEDERATED_STORAGE_ENGINE=1 \
-DFORCE_INSOURCE_BUILD=1 \
-DFORCE_COLORED_OUTPUT=NO \
-DWITH_BOOST=boost -LH
#检查通过后执行编译安装
sudo make V=2 -j 2
sudo make V=2 install
```

### 6. 生成配置文件 <a name="conf"></a>

+ server

```toml
#服务端基本设置
[mysqld]
#MySQL监听端口
port = 33061
#为MySQL客户端程序和服务器之间的本地通讯指定一个套接字文件
socket = /mnt/mysql/33061/mysql.sock
#pid文件所在目录
pid-file = /mnt/mysql/33061/mysql.pid
#使用该目录作为根目录（安装目录）
basedir = /mnt/mysql/mysql-executable
#数据文件存放的目录
datadir = /mnt/mysql/33061/data
#MySQL存放临时文件的目录
tmpdir = /mnt/mysql/33061/tmp
#服务端默认编码（数据库级别）
character_set_server = utf8mb4
#服务端默认的比对规则，排序规则
collation_server = utf8mb4_bin
#MySQL启动用户
user = mysql
#InnoDB 系统表空间数据文件 的目录路径
innodb_data_home_dir = /mnt/mysql/33061/innodb
#This variable applies when binary logging is enabled. 
#It controls whether stored function creators can be trusted not to create stored functions that will cause 
#unsafe events to be written to the binary log. 
#If set to 0 (the default), users are not permitted to create or alter stored functions unless they have the SUPER 
#privilege in addition to the CREATE ROUTINE or ALTER ROUTINE privilege. 开启了binlog后，必须设置这个值为1.主要是考虑binlog安全
log_bin_trust_function_creators = 1
#性能优化的引擎，默认关闭
performance_schema = 0
#secure_auth 为了防止低版本的MySQL客户端(<4.1)使用旧的密码认证方式访问高版本的服务器。MySQL 5.6.7开始secure_auth 默认为启用值1
secure_auth = 1
#开启全文索引
#ft_min_word_len = 1
#自动修复MySQL的myisam表
#myisam_recover
#明确时间戳默认null方式
explicit_defaults_for_timestamp
#计划任务（事件调度器）
event_scheduler
#跳过外部锁定;External-locking用于多进程条件下为MyISAM数据表进行锁定
skip-external-locking
#跳过客户端域名解析；当新的客户连接mysqld时，mysqld创建一个新的线程来处理请求。该线程先检查是否主机名在主机名缓存中。如果不在，线程试图解析主机名。
#使用这一选项以消除MySQL进行DNS解析的时间。但需要注意，如果开启该选项，则所有远程主机连接授权都要使用IP地址方式，否则MySQL将无法正常处理连接请求!
skip-name-resolve
#MySQL绑定IP
#bind-address = 127.0.0.1
#为了安全起见，复制环境的数据库还是设置--skip-slave-start参数，防止复制随着mysql启动而自动启动
skip-slave-start 
 
#The number of seconds to wait for more data from a master/slave connection before aborting the read. MySQL主从复制的时候，
slave_net_timeout = 30  
 
#当Master和Slave之间的网络中断，但是Master和Slave无法察觉的情况下（比如防火墙或者路由问题）。
#Slave会等待slave_net_timeout设置的秒数后，才能认为网络出现故障，然后才会重连并且追赶这段时间主库的数据。
#1.用这三个参数来判断主从是否延迟是不准确的Slave_IO_Running,Slave_SQL_Running,Seconds_Behind_Master.还是用pt-heartbeat吧。
#2.slave_net_timeout不要用默认值，设置一个你能接受的延时时间。
#设定是否支持命令load data local infile。如果指定local关键词，则表明支持从客户主机读文件
local-infile = 0
 
#指定MySQL可能的连接数量。当MySQL主线程在很短的时间内得到非常多的连接请求，该参数就起作用，之后主线程花些时间（尽管很短）检查连接并且启动一个新线程。
#back_log参数的值指出在MySQL暂时停止响应新请求之前的短时间内多少个请求可以被存在堆栈中。
back_log = 1024
 
#sql_mode,定义了mysql应该支持的sql语法，数据校验等!  NO_AUTO_CREATE_USER：禁止GRANT创建密码为空的用户。
#sql_mode = 'PIPES_AS_CONCAT,ANSI_QUOTES,IGNORE_SPACE,NO_KEY_OPTIONS,NO_TABLE_OPTIONS,NO_FIELD_OPTIONS,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION'
 
#NO_ENGINE_SUBSTITUTION 如果需要的存储引擎被禁用或未编译，可以防止自动替换存储引擎
#STRICT_TRANS_TABLES,NO_AUTO_CREATE_USER,NO_AUTO_VALUE_ON_ZERO,NO_ENGINE_SUBSTITUTION,STRICT_ALL_TABLES
sql_mode = NO_ENGINE_SUBSTITUTION,NO_AUTO_CREATE_USER
#索引块的缓冲区大小，对MyISAM表性能影响最大的一个参数.决定索引处理的速度，尤其是索引读的速度。默认值是16M，通过检查状态值Key_read_requests
#和Key_reads，可以知道key_buffer_size设置是否合理
key_buffer_size = 32M
 
#一个查询语句包的最大尺寸。消息缓冲区被初始化为net_buffer_length字节，但是可在需要时增加到max_allowed_packet个字节。
#该值太小则会在处理大包时产生错误。如果使用大的BLOB列，必须增加该值。
#这个值来限制server接受的数据包大小。有时候大的插入和更新会受max_allowed_packet 参数限制，导致写入或者更新失败。
max_allowed_packet = 512M
 
#线程缓存；主要用来存放每一个线程自身的标识信息，如线程id，线程运行时基本信息等等，我们可以通过 thread_stack 参数来设置为每一个线程栈分配多大的内存。
thread_stack = 256K
 
#是MySQL执行排序使用的缓冲大小。如果想要增加ORDER BY的速度，首先看是否可以让MySQL使用索引而不是额外的排序阶段。
#如果不能，可以尝试增加sort_buffer_size变量的大小。
sort_buffer_size = 16M 
 
#是MySQL读入缓冲区大小。对表进行顺序扫描的请求将分配一个读入缓冲区，MySQL会为它分配一段内存缓冲区。read_buffer_size变量控制这一缓冲区的大小。
#如果对表的顺序扫描请求非常频繁，并且你认为频繁扫描进行得太慢，可以通过增加该变量值以及内存缓冲区大小提高其性能。
read_buffer_size = 16M
 
#应用程序经常会出现一些两表（或多表）Join的操作需求，MySQL在完成某些 Join 需求的时候（all/index join），为了减少参与Join的“被驱动表”的 
#读取次数以提高性能，需要使用到 Join Buffer 来协助完成 Join操作。当 Join Buffer 太小，MySQL 不会将该 Buffer 存入磁盘文件， #而是先将Join Buffer中的结果集与需要 Join 的表进行 Join 操作， #然后清空 Join Buffer 中的数据，继续将剩余的结果集写入此 Buffer 中，如此往复。这势必会造成被驱动表需要被多次读取，成倍增加 IO 访问，降低效率。
join_buffer_size = 16M
 
#是MySQL的随机读缓冲区大小。当按任意顺序读取行时(例如，按照排序顺序)，将分配一个随机读缓存区。进行排序查询时，MySQL会首先扫描一遍该缓冲，以避免磁盘搜索，
#提高查询速度，如果需要排序大量数据，可适当调高该值。但MySQL会为每个客户连接发放该缓冲空间，所以应尽量适当设置该值，以避免内存开销过大。
read_rnd_buffer_size = 32M
 
#通信缓冲区在查询期间被重置到该大小。通常不要改变该参数值，但是如果内存不足，可以将它设置为查询期望的大小。
#（即，客户发出的SQL语句期望的长度。如果语句超过这个长度，缓冲区自动地被扩大，直到max_allowed_packet个字节。）
net_buffer_length = 16K 
 
  
#当对MyISAM表执行repair table或创建索引时，用以缓存排序索引；设置太小时可能会遇到” myisam_sort_buffer_size is too small”
myisam_sort_buffer_size = 128M
#默认8M，当对MyISAM非空表执行insert … select/ insert … values(…),(…)或者load data infile时，使用树状cache缓存数据，每个thread分配一个；
#注：当对MyISAM表load 大文件时，调大bulk_insert_buffer_size/myisam_sort_buffer_size/key_buffer_size会极大提升速度 
bulk_insert_buffer_size = 32M  
#thread_cahe_size线程池，线程缓存。用来缓存空闲的线程，以至于不被销毁，如果线程缓存在的空闲线程，需要重新建立新连接，
#则会优先调用线程池中的缓存，很快就能响应连接请求。每建立一个连接，都需要一个线程与之匹配。
thread_cache_size = 384   
#工作原理： 一个SELECT查询在DB中工作后，DB会把该语句缓存下来，当同样的一个SQL再次来到DB里调用时，DB在该表没发生变化的情况下把结果从缓存中返回给Client。
#在数据库写入量或是更新量也比较大的系统，该参数不适合分配过大。而且在高并发，写入量大的系统，建系把该功能禁掉。
query_cache_size = 0    
 
#决定是否缓存查询结果。这个变量有三个取值：0,1,2，分别代表了off、on、demand。
query_cache_type = 0    

#它规定了内部内存临时表的最大值，每个线程都要分配。（实际起限制作用的是tmp_table_size和max_heap_table_size的最小值。）
#如果内存临时表超出了限制，MySQL就会自动地把它转化为基于磁盘的MyISAM表，存储在指定的tmpdir目录下
tmp_table_size = 1024M
#独立的内存表所允许的最大容量.# 此选项为了防止意外创建一个超大的内存表导致永尽所有的内存资源.
max_heap_table_size = 512M     
#mysql打开最大文件数
open_files_limit = 10240 
 
#MySQL无论如何都会保留一个用于管理员（SUPER）登陆的连接，用于管理员连接数据库进行维护操作，即使当前连接数已经达到了max_connections。
#因此MySQL的实际最大可连接数为max_connections+1；
#这个参数实际起作用的最大值（实际最大可连接数）为16384，即该参数最大值不能超过16384，即使超过也以16384为准；
#增加max_connections参数的值，不会占用太多系统资源。系统资源（CPU、内存）的占用主要取决于查询的密度、效率等；
#该参数设置过小的最明显特征是出现”Too many connections”错误；
max_connections = 2000
 
#用来限制用户资源的，0不限制；对整个服务器的用户限制
max-user-connections = 0
 
#max_connect_errors是一个MySQL中与安全有关的计数器值，它负责阻止过多尝试失败的客户端以防止暴力破解密码的情况。max_connect_errors的值与性能并无太大关系。
#当此值设置为10时，意味着如果某一客户端尝试连接此MySQL服务器，但是失败（如密码错误等等）10次，则MySQL会无条件强制阻止此客户端连接。
max_connect_errors = 100000 
 
#表描述符缓存大小，可减少文件打开/关闭次数
table_open_cache = 5120
 
#interactive_time -- 指的是mysql在关闭一个交互的连接之前所要等待的秒数(交互连接如mysql gui tool中的连接）
interactive_timeout = 86400
#wait_timeout -- 指的是MySQL在关闭一个非交互的连接之前所要等待的秒数
wait_timeout = 86400
 
#二进制日志缓冲大小 
#我们知道InnoDB存储引擎是支持事务的，实现事务需要依赖于日志技术，为了性能，日志编码采用二进制格式。那么，我们如何记日志呢？有日志的时候，就直接写磁盘？
#可是磁盘的效率是很低的，如果你用过Nginx，，一般Nginx输出access log都是要缓冲输出的。因此，记录二进制日志的时候，我们是否也需要考虑Cache呢？
#答案是肯定的，但是Cache不是直接持久化，于是面临安全性的问题——因为系统宕机时，Cache中可能有残余的数据没来得及写入磁盘。因此，Cache要权衡，要恰到好处：
#既减少磁盘I/O，满足性能要求；又保证Cache无残留，及时持久化，满足安全要求。
binlog_cache_size = 16M
 
#开启慢查询
slow_query_log = 1
 
#超过的时间为1s；MySQL能够记录执行时间超过参数 long_query_time 设置值的SQL语句，默认是不记录的。
long_query_time = 1
 
#记录管理语句和没有使用index的查询记录
log-slow-admin-statements 
log-queries-not-using-indexes
 
# *** Replication related settings ***
#在复制方面的改进就是引进了新的复制技术：基于行的复制。简言之，这种新技术就是关注表中发生变化的记录，而非以前的照抄 binlog 模式。
#从 MySQL 5.1.12 开始，可以用以下三种模式来实现：基于SQL语句的复制(statement-based replication, SBR)，基于行的复制(row-based replication, RBR)，混合模式复制(mixed-based replication, MBR)。相应地，binlog的格式也有三种：STATEMENT，ROW，MIXED。MBR 模式中，SBR 模式是默认的。
binlog_format = ROW
 
# 为每个session 最大可分配的内存，在事务过程中用来存储二进制日志的缓存。
#max_binlog_cache_size = 102400
#开启二进制日志功能，binlog数据位置
log-bin = /mnt/mysql/33061/binlog/mysql-bin
log-bin-index = /mnt/mysql/33061/binlog/mysql-bin.index
#relay-log日志记录的是从服务器I/O线程将主服务器的二进制日志读取过来记录到从服务器本地文件，
#然后SQL线程会读取relay-log日志的内容并应用到从服务器
#binlog传到备机被写道relaylog里，备机的slave sql线程从relaylog里读取然后应用到本地。
relay-log = /mnt/mysql/33061/relay/mysql-relay-bin
relay-log-index = /mnt/mysql/33061/relay/mysql-relay-bin.index  
 
#服务端ID，用来高可用时做区分
server_id = 100
#log_slave_updates是将从服务器从主服务器收到的更新记入到从服务器自己的二进制日志文件中。
log_slave_updates = 1 
#二进制日志自动删除的天数。默认值为0,表示“没有自动删除”。启动时和二进制日志循环时可能删除。
expire-logs-days = 15 
#如果二进制日志写入的内容超出给定值，日志就会发生滚动。你不能将该变量设置为大于1GB或小于4096字节。 默认值是1GB。
max_binlog_size = 512M    
 
#replicate-wild-ignore-table参数能同步所有跨数据库的更新，比如replicate-do-db或者replicate-ignore-db不会同步类似 
replicate-wild-ignore-table = mysql.%
#设定需要复制的Table
#replicate-wild-do-table = db_name.%
#复制时跳过一些错误;不要胡乱使用这些跳过错误的参数，除非你非常确定你在做什么。当你使用这些参数时候，MYSQL会忽略那些错误，
#这样会导致你的主从服务器数据不一致。
#slave-skip-errors = 1062,1053,1146
 
#这两个参数一般用在主主同步中，用来错开自增值, 防止键值冲突
auto_increment_offset = 1
auto_increment_increment = 2
 
#将中继日志的信息写入表:mysql.slave_realy_log_info
relay_log_info_repository = TABLE
#将master的连接信息写入表：mysql.salve_master_info
master_info_repository = TABLE 
#中继日志自我修复；当slave从库宕机后，假如relay-log损坏了，导致一部分中继日志没有处理，则自动放弃所有未执行的relay-log，
#并且重新从master上获取日志，这样就保证了relay-log的完整性
relay_log_recovery = on
# *** innodb setting ***
#InnoDB 用来高速缓冲数据和索引内存缓冲大小。 更大的设置可以使访问数据时减少磁盘 I/O。
innodb_buffer_pool_size = 4G
 
#单独指定数据文件的路径与大小 可选ibdata1:32M;ibdata2:16M:autoextend
innodb_data_file_path = ibdata1:1G:autoextend
innodb_temp_data_file_path = ibtmp1:1G:autoextend:max:30G
 
#每次commit 日志缓存中的数据刷到磁盘中。通常设置为 1，意味着在事务提交前日志已被写入磁盘， 事务可以运行更长以及服务崩溃后的修复能力。
#如果你愿意减弱这个安全，或你运行的是比较小的事务处理，可以将它设置为 0 ，以减少写日志文件的磁盘 I/O。这个选项默认设置为 0。
innodb_flush_log_at_trx_commit = 0

innodb_checksum_algorithm = strict_crc32
 
#sync_binlog=n，当每进行n次事务提交之后，MySQL将进行一次fsync之类的磁盘同步指令来将binlog_cache中的数据强制写入磁盘。
#sync_binlog = 1000
 
#对于多核的CPU机器，可以修改innodb_read_io_threads和innodb_write_io_threads来增加IO线程，来充分利用多核的性能
innodb_read_io_threads = 8
innodb_write_io_threads = 8
 
#Innodb Plugin引擎开始引入多种格式的行存储机制，目前支持：Antelope、Barracuda两种。其中Barracuda兼容Antelope格式。
innodb_file_format = Barracuda
 
#限制Innodb能打开的表的数量
innodb_open_files = 65536
#开始碎片回收线程。这个应该能让碎片回收得更及时而且不影响其他线程的操作
innodb_purge_threads = 1
#分布式事务
innodb_support_xa = FALSE
#InnoDB 将日志写入日志磁盘文件前的缓冲大小。理想值为 1M 至 8M。大的日志缓冲允许事务运行时不需要将日志保存入磁盘而只到事务被提交(commit)。
#因此，如果有大的事务处理，设置大的日志缓冲可以减少磁盘I/O。
innodb_log_buffer_size = 256M
 
#日志组中的每个日志文件的大小(单位 MB)。如果 n 是日志组中日志文件的数目，那么理想的数值为 1M 至下面设置的缓冲池(buffer pool)大小的 1/n。较大的值，
#可以减少刷新缓冲池的次数，从而减少磁盘 I/O。但是大的日志文件意味着在崩溃时需要更长的时间来恢复数据。
innodb_log_file_size = 1G
 
#指定有三个日志组
innodb_log_files_in_group = 3
 
#在回滚(rooled back)之前，InnoDB 事务将等待超时的时间(单位 秒)
#innodb_lock_wait_timeout = 120
 
#innodb_max_dirty_pages_pct作用：控制Innodb的脏页在缓冲中在那个百分比之下，值在范围1-100,默认为90.这个参数的另一个用处：
#当Innodb的内存分配过大，致使swap占用严重时，可以适当的减小调整这个值，使达到swap空间释放出来。建义：这个值最大在90%，最小在15%。
#太大，缓存中每次更新需要致换数据页太多，太小，放的数据页太小，更新操作太慢。
innodb_max_dirty_pages_pct = 75
#innodb_buffer_pool_size 一致 可以开启多个内存缓冲池，把需要缓冲的数据hash到不同的缓冲池中，这样可以并行的内存读写。
innodb_buffer_pool_instances = 4  
 
#这个参数据控制Innodb checkpoint时的IO能力
innodb_io_capacity = 500
 
#作用：使每个Innodb的表，有自已独立的表空间。如删除文件后可以回收那部分空间。
#分配原则：只有使用不使用。但ＤＢ还需要有一个公共的表空间。
innodb_file_per_table = 1
 
#当更新/插入的非聚集索引的数据所对应的页不在内存中时（对非聚集索引的更新操作通常会带来随机IO），会将其放到一个insert buffer中，
#当随后页面被读到内存中时，会将这些变化的记录merge到页中。当服务器比较空闲时，后台线程也会做merge操作
innodb_change_buffering = inserts
 
#该值影响每秒刷新脏页的操作，开启此配置后，刷新脏页会通过判断产生重做日志的速度来判断最合适的刷新脏页的数量；
innodb_adaptive_flushing = 1
 
#数据库事务隔离级别 ，读取提交内容
transaction-isolation = READ-COMMITTED
 
#innodb_flush_method这个参数控制着innodb数据文件及redo log的打开、刷写模式
#InnoDB使用O_DIRECT模式打开数据文件，用fsync()函数去更新日志和数据文件。
innodb_flush_method = O_DIRECT
 
#默认设置值为1.设置为0：表示Innodb使用自带的内存分配程序；设置为1：表示InnoDB使用操作系统的内存分配程序。
#innodb_use_sys_malloc = 1
 
[mysqldump]
#它强制 mysqldump 从服务器查询取得记录直接输出而不是取得所有记录后将它们缓存到内存中
quick
#限制server接受的数据包大小;指代mysql服务器端和客户端在一次传送数据包的过程当中数据包的大小
max_allowed_packet = 512M       
#TCP/IP和套接字通信缓冲区大小,创建长度达net_buffer_length的行
net_buffer_length = 16384       
 
[mysql]
#auto-rehash是自动补全的意思
auto-rehash
max_allowed_packet = 512M
socket = /mnt/mysql/33061/mysql.sock
port = 33061
#连接蛇命令提示符号
prompt="\\u@\\h : \\d \\r:\\m:\\s>"

[mysqld_safe]
user = mysql
nice = 0
#isamchk数据检测恢复工具
# [isamchk]   
# key_buffer = 256M
# sort_buffer_size = 256M
# read_buffer = 2M
# write_buffer = 2M
 
# #使用myisamchk实用程序来获得有关你的数据库桌表的信息、检查和修复他们或优化他们
# [myisamchk]
# key_buffer = 256M
# sort_buffer_size = 256M
# read_buffer = 2M
# write_buffer = 2M
 
# [mysqlhotcopy]
# #mysqlhotcopy使用lock tables、flush tables和cp或scp来快速备份数据库.它是备份数据库或单个表最快的途径,完全属于物理备份,但只能用于备份MyISAM存储引擎和运行在数据库目录所在的机器上.
# interactive-timeout
```

+ client

```shell

```

### 7. 初始化数据库<a name="init"></a>

:::info
<font color=#FFFF00 >授予目录 `mysql`用户和`mysql` 组所有权，并适当设置目录权限, <font style="color:#DF2A3F;">**注意**</font> ⚠️ 在该步骤必须确保所需目录已经创建，请参考<a href="#目录规划">目录规划</a> 获取执行一下脚本检查目录</font>
:::
```sh 
for i in binlog data tmp innodb config;do if [[ -d "$i" ]];then echo "Directory exists";else echo "Directory not exists";fi;done
```


#### 7.1 拓展 `mysqld` 数据库初始化过程 <a name="exp"></a>
一下十几个常用的参数选项
+ `--initialize` 生成随机初始 密码
+ `--initialize-insecure`不会`root`生成密码。这是不安全的；假定您打算在将服务器投入生产使用之前及时为帐户分配密码
+ `--user` `mysql`登录帐户所有，这样服务器在稍后运行时才能对其进行读写访问
+ `--basedir`MySQL 安装基目录的路径
+ `--defaults-file`  指定mysq配置文件路径
+ `--datadir` 数据文件存储路径

当使用 `--initialize`或 `--initialize-insecure`选项调用时， `mysqld`在数据目录初始化序列期间执行以下操作：

1. 服务器检查数据目录是否存在，如下所示：
    - 如果不存在数据目录，服务器将创建它。
    - 如果数据目录存在但不为空（即它包含文件或子目录），则服务器在生成错误消息后退出:

        <font style="color:#DF2A3F;"> [ERROR] --initialize specified but the data directory exists. Aborting.</font> 在这种情况下，请删除或重命名数据目录并重试。

1. 在数据目录中，服务器创建 `mysql`系统模式及其表，包括数据字典表、授权表、时区表和服务器端帮助表。请参见 [第 7.3 节“mysql 系统模式”](https://dev.mysql.com/doc/refman/8.0/en/system-schema.html)。
2. 服务器初始化 [系统表空间](https://dev.mysql.com/doc/refman/8.0/en/glossary.html#glos_system_tablespace)和管理`InnoDB`表所需的相关数据结构。  

:::info

  <font color=#FFFF00 > `mysqld`设置 `InnoDB`系统表空间 后，对表空间特征的某些更改需要设置一个全新的 实例。符合条件的更改包括系统表空间中第一个文件的文件名和撤消日志的数量。如果不想使用默认值，请确保 在运行 `mysqld`之前，MySQL配置文件`innodb_data_file_path`中的和 `innodb_log_file_size` 配置参数的设置已到位 。此外，请确保根据需要指定影响文件创建和位置的其他参数，例如 和 。 `InnoDB` `innodb_data_home_dir`  `innodb_log_group_home_dir`
如果这些选项在您的配置文件中，但该文件不在 MySQL 默认读取的位置， `--defaults-extra-file` 请在运行mysqld时使用该选项指定文件位置。</font>

:::

1. 服务器会创建一个`'root'@'localhost'` 超级用户帐户和其他保留帐户（请参阅 [第 8.2.9 节“保留帐户”](https://dev.mysql.com/doc/refman/8.0/en/reserved-accounts.html)）。一些保留帐户已被锁定，不能由客户端使用，但 `'root'@'localhost'`可供管理使用，您应该为其分配密码。

与帐户密码相关的服务器操作 `'root'@'localhost'`取决于您如何调用它：

    - 使用`--initialize</font>`但不使用 时 `--initialize-insecure</font>`，服务器会生成一个随机密码，将其标记为已过期，并写入一条显示密码的消息：

```plain
[Warning] A temporary password is generated for root@localhost:
iTag*AfrH5ej
```

    - 使用 时 `--initialize-insecure`（无论是否使用， `--initialize`因为 都`--initialize-insecure` 意味着`--initialize`），服务器不会生成密码或将其标记为已过期，并写入一条警告消息：

```plain
[Warning] root@localhost is created with an empty password ! Please
consider switching off the --initialize-insecure option.
```

有关分配新 `'root'@'localhost'`密码的说明，请参阅 初始化后根密码分配。

1. 服务器会填充用于该[HELP</font>](https://dev.mysql.com/doc/refman/8.0/en/help.html)语句的服务器端帮助表（请参见 [第 15.8.3 节“HELP 语句”</font>](https://dev.mysql.com/doc/refman/8.0/en/help.html)）。服务器不会填充时区表。要手动执行此操作，请参见 [第 7.1.15 节“MySQL 服务器时区支持”</font>](https://dev.mysql.com/doc/refman/8.0/en/time-zone-support.html)。
2. 如果[init_file</font>](https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html#sysvar_init_file)系统变量指定了 SQL 语句文件的名称，则服务器将执行文件中的语句。此选项使您能够执行自定义引导序列。

当服务器在引导模式下运行时，某些功能不可用，从而限制了文件中允许的语句。这些包括与帐户管理（例如[CREATE USER</font>](https://dev.mysql.com/doc/refman/8.0/en/create-user.html)或[GRANT</font>](https://dev.mysql.com/doc/refman/8.0/en/grant.html)）、复制和全局事务标识符相关的语句。

7. 服务器退出。

### 8. 使用`mysqld`执行初始化命令
此处不需要指定`--basedir` 和`--datadir`因为指定在了server.cnf文件中，所有信息都从这个文件读取配置 [备注: <a href="#conf">server.cnf</a> --> /mnt/mysql/33061/server.cnf]

1. 初始化第一个实例标识为33061
    ```sh
    sudo /mnt/mysql/mysql-executable/bin/mysqld --defaults-file=/mnt/mysql/33061/config/server.cnf --initialize --user=mysql
    ```
    如果初始化日志中没有出现任何`ERROR`则说明初始化成功，如下所示
    ```plain
    $ sudo /mnt/mysql/mysql-executable/bin/mysqld --defaults-file=/mnt/mysql/33061/config/server.cnf --initialize --user=mysql
    2025-03-06T00:17:05.631205Z 0 [Warning] [MY-011068] [Server] The syntax 'skip_slave_start' is deprecated and will be removed in a future release. Please use skip_replica_start instead.
    2025-03-06T00:17:05.631210Z 0 [Warning] [MY-011068] [Server] The syntax 'slave_net_timeout' is deprecated and will be removed in a future release. Please use replica_net_timeout instead.
    2025-03-06T00:17:05.631241Z 0 [Warning] [MY-011070] [Server] 'binlog_format' is deprecated and will be removed in a future release.
    2025-03-06T00:17:05.631250Z 0 [Warning] [MY-011068] [Server] The syntax 'log_slave_updates' is deprecated and will be removed in a future release. Please use log_replica_updates instead.
    2025-03-06T00:17:05.631253Z 0 [Warning] [MY-011068] [Server] The syntax 'expire-logs-days' is deprecated and will be removed in a future release. Please use binlog_expire_logs_seconds instead.
    2025-03-06T00:17:05.631262Z 0 [Warning] [MY-011069] [Server] The syntax '--relay-log-info-repository' is deprecated and will be removed in a future release.
    2025-03-06T00:17:05.631265Z 0 [Warning] [MY-011069] [Server] The syntax '--master-info-repository' is deprecated and will be removed in a future release.
    2025-03-06T00:17:05.631329Z 0 [System] [MY-013169] [Server] /mnt/mysql/mysql-executable/bin/mysqld (mysqld 8.0.40) initializing of server in progress as process 2929
    2025-03-06T00:17:05.638513Z 0 [Warning] [MY-013907] [InnoDB] Deprecated configuration parameters innodb_log_file_size and/or innodb_log_files_in_group have been used to compute innodb_redo_log_capacity=3221225472. Please use innodb_redo_log_capacity instead.
    2025-03-06T00:17:05.640180Z 1 [System] [MY-013576] [InnoDB] InnoDB initialization has started.
    2025-03-06T00:17:06.390411Z 1 [System] [MY-013577] [InnoDB] InnoDB initialization has ended.
    2025-03-06T00:17:06.830164Z 6 [Note] [MY-010454] [Server] A temporary password is generated for root@localhost: j1ktkTN%8(rl
    ```
    :::info
      <font color=#FFFF00 > 在MySQL初始化过程中会自动生成密码，如上日志显示最后一行则为 `root` 用户生成的密码 `j1ktkTN%8(rl` ,该密码还可以在日志文件中找到  `/va/log/mysql/33061-error.log` </font>
    :::
2. 初始化第二个实例标识为`33062`，初始化命令如下：
   
    ```sh
    sudo /mnt/mysql/mysql-executable/bin/mysqld --defaults-file=/mnt/mysql/33062/config/server.cnf --initialize --user=mysql
    ```
    如果初始化日志中没有出现任何`ERROR`则说明初始化成功，如下所示
    ```plain
    sudo cat /var/log/mysql/33062-error.log 
    2025-03-06T02:56:24.677058Z 0 [Warning] [MY-011068] [Server] The syntax 'skip_slave_start' is deprecated and will be removed in a future release. Please use skip_replica_start instead.
    2025-03-06T02:56:24.677068Z 0 [Warning] [MY-011068] [Server] The syntax 'slave_net_timeout' is deprecated and will be removed in a future release. Please use replica_net_timeout instead.
    2025-03-06T02:56:24.677131Z 0 [Warning] [MY-011070] [Server] 'binlog_format' is deprecated and will be removed in a future release.
    2025-03-06T02:56:24.677148Z 0 [Warning] [MY-011068] [Server] The syntax 'log_slave_updates' is deprecated and will be removed in a future release. Please use log_replica_updates instead.
    2025-03-06T02:56:24.677155Z 0 [Warning] [MY-011068] [Server] The syntax 'expire-logs-days' is deprecated and will be removed in a future release. Please use binlog_expire_logs_seconds instead.
    2025-03-06T02:56:24.677172Z 0 [Warning] [MY-011069] [Server] The syntax '--relay-log-info-repository' is deprecated and will be removed in a future release.
    2025-03-06T02:56:24.677179Z 0 [Warning] [MY-011069] [Server] The syntax '--master-info-repository' is deprecated and will be removed in a future release.
    2025-03-06T02:56:24.677297Z 0 [System] [MY-013169] [Server] /mnt/mysql/mysql-executable/bin/mysqld (mysqld 8.0.40) initializing of server in progress as process 5142
    2025-03-06T02:56:24.684313Z 0 [Warning] [MY-013907] [InnoDB] Deprecated configuration parameters innodb_log_file_size and/or innodb_log_files_in_group have been used to compute innodb_redo_log_capacity=3221225472. Please use innodb_redo_log_capacity instead.
    2025-03-06T02:56:24.685538Z 1 [System] [MY-013576] [InnoDB] InnoDB initialization has started.
    2025-03-06T02:56:25.504447Z 1 [System] [MY-013577] [InnoDB] InnoDB initialization has ended.
    2025-03-06T02:56:25.928461Z 6 [Note] [MY-010454] [Server] A temporary password is generated for root@localhost: dKX,Z?L&!3wl
    ```

    :::info
      <font color=#FFFF00 > 在MySQL初始化过程中会自动生成密码，如上日志显示最后一行则为 `root` 用户生成的密码 `dKX,Z?L&!3wl` ,该密码还可以在日志文件中找到  `/va/log/mysql/33062-error.log` </font>
    :::

### 9.使用 systemd 启动服务器

添加一个 `systemd` 服务单元配置文件，其中包含有关 `MySQL` 服务的详细信息。该文件名为 `mysqld-33061.service`，并放置在 中 `/etc/systemd/system/mysqld-33061.service`。其中`mysqld-33061.service`是为来配置多实例区分服务特殊设置名称，如果服务器只需部署一个实例则使用默认的名称例如`mysqld.service`

1. 添加端口实例为`33061`的systemctl 文件命令如下：
   
```sh
sudo vim /etc/systemd/system/mysqld-33061.service
```
```plain
[Unit]
Description=MySQL Server
Documentation=man:mysqld(7)
Documentation=http://dev.mysql.com/doc/refman/en/using-systemd.html
After=network.target
After=syslog.target

[Install]
WantedBy=multi-user.target

[Service]
User=mysql
Group=mysql

Type=forking

PIDFile=/mnt/mysql/33061/mysql.pid

# Disable service start and stop timeout logic of systemd for mysqld service.
TimeoutSec=0

# Start main service
ExecStart=/mnt/mysql/mysql-executable/bin/mysqld --defaults-file=/mnt/mysql/33061/config/server.cnf  --daemonize  --pid-file=/mnt/mysql/33061/mysql.pid $MYSQLD_OPTS 

# Use this to switch malloc implementation
EnvironmentFile=-/etc/sysconfig/mysql

# Sets open_files_limit
LimitNOFILE = 5000

Restart=on-failure

RestartPreventExitStatus=1

PrivateTmp=false
```

1. 添加端口实例为`33062`的systemctl 文件  
   
```sh
sudo vim /etc/systemd/system/mysqld-33062.service
```
```plain
[Unit]
Description=MySQL Server
Documentation=man:mysqld(7)
Documentation=http://dev.mysql.com/doc/refman/en/using-systemd.html
After=network.target
After=syslog.target

[Install]
WantedBy=multi-user.target

[Service]
User=mysql
Group=mysql

Type=forking

PIDFile=/mnt/mysql/33062/mysql.pid

# Disable service start and stop timeout logic of systemd for mysqld service.
TimeoutSec=0

# Start main service
ExecStart=/mnt/mysql/mysql-executable/bin/mysqld --defaults-file=/mnt/mysql/33062/config/server.cnf  --daemonize  --pid-file=/mnt/mysql/33062/mysql.pid $MYSQLD_OPTS 

# Use this to switch malloc implementation
EnvironmentFile=-/etc/sysconfig/mysql

# Sets open_files_limit
LimitNOFILE = 5000

Restart=on-failure

RestartPreventExitStatus=1

PrivateTmp=false
```

:::info
  <font color=#FFFF00 > 
     重要的上面的起始字符串`ExecStart`被分成两行，以适应本文档的页面宽度。将配置信息复制到文件后，将字符串恢复为一行。此外， 起始字符串`--pid-file`中的设置 `ExecStart`必须 `PIDFile`与其前面的设置相匹配。 配置文件`--pid-file`中指定的选项`my.cnf`将被 `systemd` 忽略。</font><br>
   <font color=#FFFF00 >
    特别要注意的是端口标识实例要分开，否则启动报错。</font>
:::

1. 为 systemd tmpfiles功能添加一个配置文件。该文件被命名为 mysql.conf并放置在 中 /usr/lib/tmpfiles.d。
    ```sh
    sudo mkdir /etc/systemd/system/tmpfiles.d 
    sudo vim /etc/systemd/system/tmpfiles.d/mysql-33061.conf
    ```
   - 在文件中添加以下配置信息 mysql.conf：
    ```toml
    d /mnt/mysql/33061/data 0750 mysql mysql  -
    ```
2. 使用`systemctl`命令启动MySQl服务
    ```sh
    sudo systemctl daemon-reload && sudo systemctl enable --now  mysqld-33061.service && sudo systemctl status mysqld-33061.service
    ```
    :::info
      <font color=#FFFF00 > 使用`systemctl`命令启动，可以使用 `journalctl`访问。要查看与 mysqld 相关的日志消息，请使用journalctl -u mysqld。某些消息（例如 MySQL 启动消息）可能会打印到 systemd 日志中。
    有关 systemd 的更多信息，请参阅 使用 systemd 管理 MySQL 服务器。</font>
    :::
   -   检查启动服务状态
    ```sh
    sudo systemctl status mysqld-33061.service
    ```
    如果启动成功则会输出如下状态，否则按照`sudo journalctl -u mysqld-33061.service -f 进行日志排查`
    ```plain
    ● mysqld-33061.service - MySQL Server
        Loaded: loaded (/etc/systemd/system/mysqld-33061.service; enabled; preset: disabled)
        Active: active (running) since Thu 2025-03-06 09:06:16 CST; 8min ago
        Docs: man:mysqld(7)
                http://dev.mysql.com/doc/refman/en/using-systemd.html
        Process: 3912 ExecStart=/mnt/mysql/mysql-executable/bin/mysqld --defaults-file=/mnt/mysql/33061/config/server.cnf --daemonize --pid-file=/mnt/mysql/33061/mysql.pid $MYSQLD_OPTS (code=exited>
        Main PID: 3914 (mysqld)
        Tasks: 45 (limit: 54770)
        Memory: 743.2M
            CPU: 6.561s
        CGroup: /system.slice/mysqld-33061.service
                └─3914 /mnt/mysql/mysql-executable/bin/mysqld --defaults-file=/mnt/mysql/33061/config/server.cnf --daemonize --pid-file=/mnt/mysql/33061/mysql.pid

    Mar 06 09:06:16 CloudDB-LllrVWYZvXdzezE3BK9w systemd[1]: Starting MySQL Server...
    Mar 06 09:06:16 CloudDB-LllrVWYZvXdzezE3BK9w systemd[1]: Started MySQL Server.
    ```
### 10. 测试数据库连接和更新root默认密码

通过以上操作后，两个实例分别为`33061`,`33062`初始化且服务启动成功，需要为数据库更新`root`密码是操作如下
:::info
  <font color=#FFFF00 > 在执行一下命令会用到mysql 这个编译好的二进制文件，此处我添加软连接到 `PATH` 中 `sudo ln -s /mnt/mysql/mysql-executable/bin/mysql_config_editor /usr/local/bin/` 这样就避免使用绝对路径，减少操作 </font>
  :::

1. 修改实例为`33061`密码
   - 登录数据库
    ```sh
     mysql -uroot -p -S /mnt/mysql/33061/mysql.sock
    ```
   - 更新`root`密码 
    ```sql
    mysql> ALTER USER 'root'@'localhost' IDENTIFIED BY 'new_password';
    mysql> flush privileges;
    ```
2. 修改实例为`33062`密码
   - 登录数据库
    ```sh
     mysql -uroot -p -S /mnt/mysql/33062/mysql.sock
    ```
   - 更新`root`密码 
    ```sql
    mysql> ALTER USER 'root'@'localhost' IDENTIFIED BY 'new_password';
    mysql> flush privileges;
    ```

    
mysql_config_editor set --login-path=33062 --host=localhost --user=root --password --port=33062 --socket=/mnt/mysql/33062/mysql.sock

[https://dev.mysql.com/doc/refman/8.0/en/data-directory-initialization.html](https://dev.mysql.com/doc/refman/8.0/en/data-directory-initialization.html)


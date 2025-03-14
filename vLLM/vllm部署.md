#  RYA vLLM 
vLLM 是一个Python库，它还包含预编译的c++和CUDA(12.1)二进制文件

## 2. 安装要求<a name="yq-2025-03"></a>

 - 操作系统 Linux-Ubuntu-22.04.5 LTS (Jammy Jellyfish)
 - Python 3.8-2.12
 - GPU: 计算能力7.0或更高(例如,v100,T4,RTX20xx,A100,L4,H100等)

本次测试安装环境如下：
<table>
    <tr>
        <th>IP</th>
        <th>系统</th>
        <th>安装软件</th>
        <th>工具依赖</th>
    </tr>
     <tr>
        <td >192.168.8.102</td>
        <td rowspan="8">Linux version 5.15.0-134-generic (buildd@lcy02-amd64-081)<br>(gcc (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0, <br>GNU ld (GNU Binutils for Ubuntu) 2.38) #145-Ubuntu SMP Wed Feb 12 20:08:39 UTC 2025</td>
        <td rowspan="8">Python3.10<br>NVIDIA-Linux-x86_64-550.135<br>cuda_12.4.0_550.54.14</td>
        <td rowspan="8">wget; cmake >=3.26; vim</td>
    </tr>
    <tr>
         <td >192.168.8.113</td>
    </tr>
       <tr>
         <td >192.168.8.115</td>
    </tr>
       <tr>
         <td >192.168.8.106</td>
    </tr>
       <tr>
         <td >192.168.8.107</td>
    </tr>
        </tr>
       <tr>
         <td >192.168.8.108</td>
    </tr>
        </tr>
       <tr>
         <td >192.168.8.109</td>
    </tr>
        </tr>
       <tr>
         <td >192.168.8.110</td>
    </tr>
</table>


## 3. 安装NVIDIA显卡驱动


<details open>
<summary><font style="font-size: initial;color: bisque">Install CUDA and NVIDIA (All nodes)</font> </summary>

> [!TIP]  
> 官网下载地址，按照自己环境下载指定架构哦以及版本  [NVIDIA](https://developer.nvidia.com/cuda-12-4-0-download-archive?target_os=Linux&target_arch=x86_64&Distribution=Ubuntu&target_version=22.04&target_type=runfile_local)    [CUDA](https://download.nvidia.com/XFree86/Linux-x86_64/550.135/)   [CUDA-Doc](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/#pre-installation-actions)    [NVIDIA-Doc]()

以下是基于 [要求](#2-要求)执行

```sh
#创建临时目录
mkdir /tmp/nvidia && cd $_
#下载安装程序和程序校验
wget -c \
https://download.nvidia.com/XFree86/Linux-x86_64/550.135/NVIDIA-Linux-x86_64-550.135.run \
https://download.nvidia.com/XFree86/Linux-x86_64/550.135/NVIDIA-Linux-x86_64-550.135.run.sha256sum \
https://developer.download.nvidia.com/compute/cuda/12.4.0/local_installers/cuda_12.4.0_550.54.14_linux.run \
https://developer.download.nvidia.cn/compute/cuda/12.4.0/docs/sidebar/md5sum.txt

#校验文件
echo "`cat md5sum.txt|grep cuda_12.4.0_550.54.14_linux.run`"|md5sum -c && echo "`cat NVIDIA-Linux-x86_64-550.135.run.sha256sum`" |sha256sum -c
#如果为ok则说明文件完整

#执行安装
sudo chmod +x cuda_12.4.0_550.54.14_linux.run NVIDIA-Linux-x86_64-550.135.run
sudo ./NVIDIA-Linux-x86_64-550.135.run  && sudo ./cuda_12.4.0_550.54.14_linux.run

#安装后检查
#NVIDIA显卡驱动检查
nvidia-smi
#cuda 检查
nvcc -V

#添加环境变量(注意安装路径可在=/usr/local/cuda-***,每个环节所需版本不一致，所以要按照实际版本替换即可)

#零时生效(当前终端，退出后失效)
export PATH=/usr/local/cuda-12.4/bin${PATH:+:${PATH}} 
export LD_LIBRARY_PATH=/usr/local/cuda-12.4/lib64 ${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}

#永久生效以及所有用户生效
sudo tee -a /etc/profile.d/nviidia.sh << "TOF"
export PATH=/usr/local/cuda-12.4/bin${PATH:+:${PATH}} 
export LD_LIBRARY_PATH=/usr/local/cuda-12.4/lib64 ${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
TOF
```

</details>


## 4. conda
<details open>
<summary><font style="font-size: initial;color: bisque">Install conda (All nodes)</font> </summary>

Conda 是一个强大的命令行工具，用于在 Windows、macOS 和 Linux 上运行的包和环境管理。conda启动和使用 conda 创建环境
本次采用`Miniforge`方式，关于`Miniforge`等介绍请参考官网文档说明[conda-Miniforge](https://conda-forge.org/docs/)
```sh
#下载安装文件
wget -c -v https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-x86_64.sh -O  miniforge.sh

#如果要默认安装则执行一下命令，（需要指定则更改`"${HOME}/conda"`对你对应的路径即可）
bash miniforge.sh -b -p "${HOME}/conda" && rm ./miniforge.sh

#当前环境生效
source "${HOME}/conda/etc/profile.d/conda.sh"
# For mamba support also run the following command
source "${HOME}/conda/etc/profile.d/mamba.sh"

#写入~/.bashrc
tee -a ~/.bashrc << "TOF"
source "${HOME}/conda/etc/profile.d/conda.sh"
source "${HOME}/conda/etc/profile.d/mamba.sh"
TOF

#检查是否安装成功
conda --version && conda update conda
```

> [!TIP]
> 更多命令请参考 官方文档 [conda cli](https://docs.conda.io/projects/conda/en/stable/commands/index.html) 

</details>

## 5. 基于`RAY`框架

<details open>
<summary><font style="font-size: initial;color: bisque">Ray Concept</font> </summary>

Ray 是一个开源统一框架，用于扩展 AI 和 Python 应用程序（如机器学习）。它提供了用于并行处理的计算层，因此您无需成为分布式系统专家。Ray 使用以下组件最大限度地降低了运行分布式单个和端到端机器学习工作流的复杂性：
- 可扩展的库，用于常见的机器学习任务，例如数据预处理、分布式训练、超参数调整、强化学习和模型服务。
-  用于并行化和扩展 Python 应用程序的 Pythonic 分布式计算原语。
- 用于将 Ray 集群与现有工具和基础设施（例如 Kubernetes、AWS、GCP 和 Azure）集成并部署的集成和实用程序。
- 对于数据科学家和机器学习从业者来说，Ray 可以让你扩展作业而无需基础设施专业知识：
- 轻松在多个节点和 GPU 之间并行化和分配 ML 工作负载。
- 利用具有本机和可扩展集成的 ML 生态系统。
对于 ML 平台构建者和 ML 工程师，Ray：
- 提供计算抽象以创建可扩展且强大的 ML 平台。
- 提供统一的 ML API，简化加入和与更广泛的 ML 生态系统的集成。
- 通过使相同的 Python 代码从笔记本电脑无缝扩展到大型集群，减少开发和生产之间的摩擦。
- 对于分布式系统工程师，Ray 自动处理关键流程：
- 编排——管理分布式系统的各个组件。
- 调度——协调执行任务的时间和地点。
- 容错——无论不可避免的故障点如何，都能确保任务完成。
- 自动扩展——根据动态需求调整分配的资源数量。

Ray 目前正式支持 x86_64、Linux 的 aarch64 (ARM) 和 Apple silicon (M1) 硬件。Windows 上的 Ray 目前处于测试阶段。通过一下选项来选择合适的安装
| 命令 | 已安装的组件 |
|:-----:|:------------:|
|`pip install -U "ray"`|核|
|`pip install -U "ray[default]"`|核心、仪表板、集群启动器|
|`pip install -U "ray[data]"`|核心、数据|
|`pip install -U "ray[train]"`|核心，训练|
|`pip install -U "ray[tune]"`|核心，调音|
|`pip install -U "ray[serve]"`|核心、仪表板、集群启动器、服务|
|`pip install -U "ray[serve-grpc]"`|核心、仪表板、集群启动器、支持 gRPC 的服务|
|`pip install -U "ray[rllib]"`|核心、调整、RLlib|
|`pip install -U "ray[all]"`|核心、仪表板、集群启动器、数据、训练、调整、服务、RLlib。不推荐使用此选项。请按如下所示指定所需的附加项。|
此处安装`pip install -U "ray[default]"`这个作为默认的
</details>

`Ray Cluster` 是由一个头节点(head)和任意数量的工作节点(work)组成

<details open>
<summary><font style="font-size: initial;color: bisque">Install Ray  (All nodes)</font> </summary>

```sh
#使用conda 创建一个环境
conda create -n ray-project python=3.10 -y
#切换到ray-project环境
conda activate ray-project
#安装ray相关组件
pip install --default-timeout=100 -U "ray[default]"
```
</details>


<details open>
<summary><font style="font-size: initial;color: bisque">Config RAY Cluster</font> </summary>

> [!NOTE]
>  Head 节点 也就是10.192.168.8.102

<table>
    <tr>
        <th>node IP</th>
        <th>command</th>
        <th>notes</th>
    </tr>
     <tr>
        <td >192.168.8.102</td>
        <td rowspan="5">conda activate ray-project && ray start --disable-usage-stats --head --port=8377  --node-ip-address=192.168.8.102 --num-gpus=48 --dashboard-host=192.168.8.102 --dashboard-port=8378 --metrics-export-port=8379</td>
        <td rowspan="5"> conda 切换到 ray-project 环境执行 ray 命令</td>
    </tr>
    </tr>
</table>

```plantuml
 --disable-usage-stats     禁用收集使用统计数据详见官网(https://docs.ray.io/en/master/cluster/usage-stats.html)
 --head:                   表明当前节点为head(头)节点
 --port:                   进程的端口。如果不提供，默认为 6379；如果端口设置为 0，我们将分配一个可用的端口
 --node-ip-address         当前节点的IP地址
 --num-gpus                此节点上的 GPU 数量
 --dashboard-host          将仪表板服务器绑定到的主机，可以是 localhost (127.0.0.1) 或 0.0.0.0（可从所有接口访问）。默认情况下，此主机为 127.0.0.1
 --dashboard-port          绑定仪表板服务器的端口 - 默认为 8265
 --include-dashboard       启用Ray仪表盘GUI(可选)
```
</details>

<details open>
<summary><font style="font-size: initial;color: bisque">执行上面启动命令后，如果正常则输入一下信息</font> </summary>

```plantuml
Usage stats collection is disabled.
Local node IP: 192.168.8.102

--------------------
Ray runtime started.
--------------------

Next steps
  To add another node to this Ray cluster, run
    ray start --address='192.168.8.102:8377'              #node也就是work节点加入到当前head cluset中
  
  To connect to this Ray cluster:
    import ray
    ray.init(_node_ip_address='192.168.8.102')
  
  To submit a Ray job using the Ray Jobs CLI:
    RAY_ADDRESS='http://192.168.8.102:8378' ray job submit --working-dir . -- python my_script.py
  
  See https://docs.ray.io/en/latest/cluster/running-applications/job-submission/index.html 
  for more information on submitting Ray jobs to the Ray cluster.
  
  To terminate the Ray runtime, run
    ray stop                                            #停止ray cluster
  
  To view the status of the cluster, use
    ray status                                          #输出当前ray cluster 状态
  
  To monitor and debug Ray, view the dashboard at 
    192.168.8.102:8378                                    #dashboard web页面地址和端口
  
  If connection to the dashboard fails, check your firewall settings and network configuration.
```
</details>

<details open>
<summary><font style="font-size: initial;color: bisque">Ray node joins the current cluster</font> </summary>

下图为节点信息

<table>
    <tr>
        <th>node IP</th>
        <th>command</th>
        <th>notes</th>
    </tr>
     <tr>
        <td >192.168.8.102</td>
        <td rowspan="5">conda activate ray-project && ray start --address='192.168.8.102:8377' --num-gpus=8 </td>
        <td rowspan="5"> conda 切换到 ray-project 环境执行 ray 命令</td>
    </tr>
    <tr>
         <td >192.168.8.103</td>
    </tr>
       <tr>
         <td >192.168.8.105</td>
    </tr>
       <tr>
         <td >192.168.8.106</td>
    </tr>
       <tr>
         <td >192.168.8.107</td>
    </tr>
</table>

```plantuml
 --num-gpus                 node节点上的 GPU 数量
 --address                  node节点IP地址(bond)
```
</details>

每个节点执行命令加入 ray Cluster head(192.168.8.102)

<details open>
<summary><font style="font-size: initial;color: bisque">执行加入 ray cluster 命令后，如果正常则输入一下信息</font> </summary>

```plantuml
Local node IP: 192.168.8.103
[2025-03-13 13:22:15,992 W 16686 16686] global_state_accessor.cc:429: Retrying to get node with node ID 4a43adca9417e184f0dd7277f886b83a34e1ec0a175e03faa04d94d8

--------------------
Ray runtime started.
--------------------

To terminate the Ray runtime, run
  ray stop

```
</details>

如果按照以上操作，在没有任何报错到情况下，那么恭喜您安装`Ray Cluster`集群成功，可以访问http://192.168.8.102:8378 进行操作，或者继续深入研究ray框架官网地址为[RAY](https://docs.ray.io/en/latest/ray-overview/index.html)


## 3.3 VLLM deploys distributed loads based on ray framework

<details open>
<summary><font style="font-size: initial;color: bisque">使用conda创建环境</font> </summary>

```sh
# (Recommended) Create a new conda environment.
conda create -n vllm-porject python=3.10 -y
conda activate vllm-porject
#conda remove --name ENV_NAME --all  #删除创建环境
```
</details>

>
<details open>
<summary><font style="font-size: initial;color: bisque">设置环境变量</font> </summary>

> [!NOTE]
> 将一下变量导出到当前用户`~/.bashrc`文件中，也可设置临时变量

```sh
tee -a ~/.bashrc << "TOF"
export GLOO_SOCKET_IFNAME=bond0 #来指定 IP 地址的网络接口。
export VLLM_LOGGING_LEVEL=DEBUG #以开启更多日志记录。
export CUDA_LAUNCH_BLOCKING=1 #以准确了解哪个 CUDA 内核导致了问题。
export NCCL_DEBUG=TRACE #以开启更多 NCCL 日志记录。
export VLLM_TRACE_FUNCTION=1 #vLLM 中的所有函数调用都将被记录。检查这些日志文件，并确定哪个函数崩溃或挂起。
TOF

```
</details>

<details open>
    <summary><font style="font-size: initial;color: bisque">Install vLLM with CUDA 12.1</font> </summary>
<table>
    <tr>
        <th>node IP</th>
        <th>command</th>
        <th>notes</th>
    </tr>
     <tr>
        <td >192.168.8.102</td>
        <td rowspan="5">pip install vllm --default-timeout=100</td>
        <td rowspan="5"> conda 切换到 vllm-project 环境</td>
    </tr>
    </tr>
</table>


```plantuml
# 如果安装则显示如下信息包括版本以及大小
Using cached vllm-0.7.3-cp38-abi3-manylinux1_x86_64.whl (264.6 MB)
Installing collected packages: vllm
Successfully installed vllm-0.7.3
```
</details>


<details open>
<summary><font style="font-size: initial;color: bisque">Use Python start vllm server</font> </summary>


</details>

```sh
PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True python3 -m vllm.entrypoints.openai.api_server --model $HOME/lvvm-pkg/DeepSeek-R1 --served-model-name DeepSeek-R1-70B \
  --tensor-parallel-size 8 \
  --trust-remote-code \
  --host 0.0.0.0 \
  --port 9000 \
  --max-model-len 8192 \
  --max-num-batched-tokens 16384 \
  --disable-log-requests \
  --gpu-memory-utilization 0.95
```
或者一下脚本
```sh
#! /bin/bash

set -aox

export TORCH_USE_CUDA_DSA=1
export PYTORCH_CUDA_TORCH_USE_CUDA_DSA=1
#export PYTORCH_CUDA_ALLOC_CONF=max_split_size_mb:192
export PYTORCH_NVML_BASED_CUDA_CHECK=1
export PYTORCH_NO_CUDA_MEMORY_CACHING=1
export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True
export CUDA_VISIBLE_DEVICES='[0,1,2,3,4,5,6,7]'

#--tensor-parallel-size 6 \

python3.10 -m vllm.entrypoints.openai.api_server \
--model $HOME/lvvm-pkg/DeepSeek-R1 \
--uvicorn-log-level debug \
--served-model-name DeepSeek-R1-70B \
--trust-remote-code \
--host 0.0.0.0 \
--port 9000 \
--max-model-len 8192 \
--device cuda \
--max-num-batched-tokens 16384 \
--disable-log-requests \
--gpu-memory-utilization 0.95 \
--enable-chunked-prefill
```

## 3.4 源码构建

> [!WARNING]
> 源码编译需要`cmake`版本3.26以上或更高版本，法则会报错`CMake 3.26 or higher is required.  You are running version 3.22.1`
> 请使用 `cmake --version` 检查版本，如果`>=3.26`则直接进行编译安装`vLLM`

<details open>
<summary><font style="font-size: initial;color: bisque">Cmake3.26 Install</font> </summary>

```sh
# A-1.使用以下命令卸载 Ubuntu 包管理器和配置提供的默认版本：
sudo apt remove --purge --auto-remove cmake

# A-2.安装准备
sudo apt update && \
sudo apt install -y software-properties-common lsb-release && \
sudo apt clean all

# A-3.获取 kitware 签名密钥的副本。
wget -O - https://apt.kitware.com/keys/kitware-archive-latest.asc 2>/dev/null | gpg --dearmor - | sudo tee /etc/apt/trusted.gpg.d/kitware.gpg >/dev/null

# A-4.将 kitware 的存储库添加到 Ubuntu Focal Fossa (20.04)、Ubuntu Bionic Beaver (18.04) 和 Ubuntu Xenial Xerus (16.04) 的源列表中。
sudo apt-add-repository "deb https://apt.kitware.com/ubuntu/ $(lsb_release -cs) main"

# A-5.最后我们可以更新并安装该cmake包。
sudo apt update
sudo apt install cmake
```
</details>


<details open>
<summary><font style="font-size: initial;color: bisque">Cmake Install The vLLM</font> </summary>


```sh
conda create -n vllm-project-`date +"%F"` python=3.10 -y
conda activate vllm-project-2025-03-12

git clone https://github.com/vllm-project/vllm.git
cd vllm
pip install -e .  # This may take 5-10 minutes.
```
> [!NOTE]
> `ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.
googleapis-common-protos 1.69.1 requires protobuf!=4.21.1,!=4.21.2,!=4.21.3,!=4.21.4,!=4.21.5,<6.0.0.dev0,>=3.20.2, but you have protobuf 6.30.0 which is incompatible.`

</details>


# 问题记录

<details open>
<summary><font style="font-size: initial;color: bisque"></font> CUDA error: out of memory</summary>

```python
import torch
device = torch.device('cuda:0')
free, total = torch.cuda.mem_get_info(device)
mem_used_MB = (total - free) / 1024 ** 2
print(mem_used_MB)
print ('''
查看GPU内容使用情况
''')
print("torch.cuda.memory_allocated: %fGB"%(torch.cuda.memory_allocated(0)/1024/1024/1024))
print("torch.cuda.memory_reserved: %fGB"%(torch.cuda.memory_reserved(0)/1024/1024/1024))
print("torch.cuda.max_memory_reserved: %fGB"%(torch.cuda.max_memory_reserved(0)/1024/1024/1024))
```
</details>
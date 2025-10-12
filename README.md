# Avilla-Lagrange

> [!IMPORTANT]  
> 不再维护。

## 重要说明

因以下原因，该项目已归档，且本人近期不再接触关于第三方bot框架的使用和开发：

* 现实因素：学习、工作；
* 关联项目处于“能用就行”的状态，使用时有些力不从心，逐渐失去兴趣；
* [这里](https://blog.fqilin.top/sthaboutlag_/)。

如果您仍对本项目感兴趣，您可以：

* Fork本项目，自己修修补补；
* 自行搜索并查阅关联项目；
* 与我联系。

## 项目介绍

该项目仅作为可行性验证：利用[Avilla](https://github.com/GraiaProject/Avilla)的抽象能力，对接[另一个bot框架](https://github.com/LagrangeDev/lagrange-python)，使两个（或多个）框架集成于同一程序中。

如需应用于生产环境，请考虑使用[avilla-onebot-v11](https://github.com/GraiaProject/Avilla/tree/master/avilla/onebot/v11)和支持[Onebot-11标准](https://github.com/botuniverse/onebot-11)的平台。

该项目未经测试，含有大量bug和未实现功能，请慎重使用。

> [!CAUTION]  
> ~~个人**完全无法知晓**Avilla及相关部件将会以什么形式重构，且未来会出现替代实现。与个人因素叠加，本项目仅作个人积累经验用。如果替代实现能够完美满足需求，本项目将即刻归档。~~

## 环境搭建

可以直接使用PDM等工具搭建，也可以参考[这个脚本](https://github.com/FZQ0003/Qi-Bot/blob/avilla/venv_script_avilla.sh)，搭建虚拟环境后把项目以软链接的形式丢进`site-packages`。

> [!NOTE]  
> 目前项目并没有在PyPI上发布，因此只能通过Git仓库安装。

```shell
pdm add git+https://github.com/FZQ0003/Avilla-Lagrange.git
```

## 已知问题

* 目前尚未实现`lagrange-python`提供的所有功能。
* 数据库定义不完善，可能会出现剧烈变动，需要手动升级或重建。
* 当前函数重载方式需要在`Avilla`使用`flywheel`重构功能后同步更新。

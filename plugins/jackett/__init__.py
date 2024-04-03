import threading
from typing import Any, Dict, List, Tuple

from app.log import logger
from app.plugins import _PluginBase


class Jackett(_PluginBase):
    # 插件名称
    plugin_name = "Jackett 索引器"
    # 插件描述
    plugin_desc = ""
    # 插件图标
    plugin_icon = ""
    # 主题色
    plugin_color = "#000000"
    # 插件版本
    plugin_version = "0.0.0"
    # 插件作者
    plugin_author = "so1ve"
    # 作者主页
    author_url = "https://github.com/so1ve"
    # 插件配置项ID前缀
    plugin_config_prefix = "jackett_"
    # 加载顺序
    plugin_order = 1
    # 可使用的用户级别
    auth_level = 1

    # 私有属性
    _enabled = False
    _delete = False
    _run_once = False
    _host = ""

    def init_plugin(self, config: dict | None = None):
        if config:
            self._enabled = bool(config.get("enabled"))
            self._api_key = bool(config.get("api_key"))
            self._host = bool(config.get("host"))
        if self._enabled:
            logger.info("Jackett 插件初始化完成")
            if self._run_once:
                thread = threading.Thread(target=self.extract, args=(self._host,))
                thread.start()
                self.update_config(
                    {
                        "enabled": self._enabled,
                        "host": self._host,
                        "api_key": False,
                    }
                )

    def get_state(self) -> bool:
        return self._enabled

    @staticmethod
    def get_command() -> List[Dict[str, Any]]:
        pass

    def get_api(self) -> List[Dict[str, Any]]:
        pass

    # 插件配置页面
    def get_form(self) -> Tuple[List[dict], Dict[str, Any]]:
        """
        拼装插件配置页面，需要返回两块数据：1、页面配置；2、数据结构
        """
        return [
            {
                "component": "VForm",
                "content": [
                    {
                        "component": "VRow",
                        "content": [
                            {
                                "component": "VCol",
                                "content": [
                                    {
                                        "component": "VSwitch",
                                        "props": {
                                            "model": "enabled",
                                            "label": "启用插件",
                                        },
                                    }
                                ],
                            },
                        ],
                    },
                    {
                        "component": "VRow",
                        "content": [
                            {
                                "component": "VCol",
                                "content": [
                                    {
                                        "component": "VTextField",
                                        "props": {
                                            "model": "host",
                                            "label": "Jackett 地址",
                                            "placeholder": "http://127.0.0.1:9117",
                                        },
                                    }
                                ],
                            },
                        ],
                    },
                    {
                        "component": "VRow",
                        "content": [
                            {
                                "component": "VCol",
                                "content": [
                                    {
                                        "component": "VTextField",
                                        "props": {
                                            "model": "api_key",
                                            "label": "Jackett API Key",
                                            "placeholder": "",
                                        },
                                    }
                                ],
                            },
                        ],
                    },
                ],
            }
        ], {
            "enabled": False,
            "api_key": "",
            "host": "",
        }

    def get_page(self) -> List[dict]:
        pass

    def stop_service(self):
        """
        退出插件
        """
        pass

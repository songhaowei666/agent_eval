#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""项目配置：从 .env 文件读取环境变量。"""

from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

# 项目根目录（config.py 所在目录）
PROJECT_ROOT = Path(__file__).resolve().parent


class Config(BaseSettings):
    """应用配置，字段与 .env 中的环境变量一一对应。"""

    model_config = SettingsConfigDict(
        env_file=PROJECT_ROOT / ".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    langsmith_api_key: str = Field(default="", description="LangSmith API 密钥")
    langchain_tracing_v2: bool = Field(default=False, description="是否启用 LangChain 追踪")
    langchain_project: str = Field(
        default="wealth-advisor-hybrid-agent",
        description="LangSmith 项目名称",
    )
    dashscope_api_key: str = Field(default="", description="DashScope API 密钥")

    openai_api_key: str = Field(default="", description="OpenAI API 密钥")
    openai_api_base: str = Field(default="https://api.openai.com/v1", description="OpenAI API 基础地址")
    chat_model: str = Field(default="gpt-4.1-mini", description="对话模型名称")

    @property
    def langsmith_enabled(self) -> bool:
        """LangSmith 是否已启用（需同时配置 API Key 且开启追踪）。"""
        return bool(self.langsmith_api_key) and self.langchain_tracing_v2


# 全局配置实例
config = Config()

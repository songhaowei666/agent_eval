# Agent Eval

AI Agent 评估与可观测性示例项目，涵盖 OpenEvals 评估器、LangSmith 测试评估、LangFuse 调用追踪。

## 目录结构

| 目录 | 说明 |
|------|------|
| `openevals_use/` | OpenEvals 内置评估器示例（正确性、简洁性、RAG、毒性等） |
| `langsmith_use/` | LangSmith 数据集、批量测试与评估 |
| `langfuse_use/` | LangFuse 集成示例（财富管理投顾 Agent） |
| `config.py` | 统一配置，从 `.env` 读取环境变量 |

## 环境配置

在项目根目录创建 `.env`：

```env
# LangSmith
LANGSMITH_API_KEY=
LANGCHAIN_TRACING_V2=true
LANGCHAIN_PROJECT=wealth-advisor-hybrid-agent

# 通义千问 / DashScope
DASHSCOPE_API_KEY=

# OpenAI（可选）
OPENAI_API_KEY=
OPENAI_API_BASE=https://api.openai.com/v1
CHAT_MODEL=gpt-4.1-mini

# LangFuse（langfuse_use 脚本需要）
LANGFUSE_PUBLIC_KEY=
LANGFUSE_SECRET_KEY=
LANGFUSE_BASE_URL=https://cloud.langfuse.com
```

安装依赖（按需）：

```bash
pip install pydantic-settings langsmith langchain-community openevals langgraph langfuse qwen-agent dashscope -i https://pypi.tuna.tsinghua.edu.cn/simple --trusted-host pypi.tuna.tsinghua.edu.cn
```

## 快速开始

```bash
# OpenEvals 单评估器示例
python openevals_use/1-correctness.py

# LangSmith 测试与评估
python langsmith_use/2-langsmith_testing_evaluation.py

# LangFuse 监测示例
python langfuse_use/1-hybrid_wealth_advisor_qwen_agent_langfuse.py
```

各脚本需在对应目录或项目根目录下运行，具体依赖见脚本内说明。

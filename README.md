## LLM Circuit generator

This demo uses [langchain custom tools](https://python.langchain.com/docs/modules/agents/tools/custom_tools
) to give ChatGPT access to executing LTSpice netlists via CLI and returning the output to the LLM.


### Setup the env

Install of [LTSpice](https://www.analog.com/en/design-center/design-tools-and-calculators/ltspice-simulator.html)

```sh
pipenv shell
```

File: `.env`
```
OPENAI_API_KEY=""
LTSPICE_PATH="C:\Users\..."
```

### Executing LTSpice

```sh
python lib.py
python llm.py
```
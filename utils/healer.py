import json
import logging
import os

from openai import OpenAI


TOKEN = os.environ.get("OPENROUTER_API_KEY", "")
# MODEL = "z-ai/glm-5.3-flash"
MODEL = "nvidia/nemotron-3-ultra-550b-a55b:free"
URL = "https://openrouter.ai/api/v1"

client = OpenAI(base_url=URL, api_key=TOKEN)


def call_llm(prompt):
    messages = [{'role': 'user', 'content': prompt}]
    logging.info(f"Sending prompt")
    response = client.chat.completions.create(model=MODEL, messages=messages)
    message = response.choices[0].message
    return message.content


def find_selector(failed_selectors, description, dom):
    prompt = (f"Please help to find correct XPATH selector for the element. "
              f"Test was trying to find it by {failed_selectors} but failed."
              f"Possibly, it's changed or missing on the page. The description of "
              f"the element is '{description}'. Here is the pages DOM: '{dom}'. "
              f"No reasoning or other text should be in the response. It should be pure JSON. ONLY JSON. "
              f"Return result in the form of JSON with this structure: "
              '{"found": bool, "selector": str}, for example {"found": true, "selector": "//*[@id="login"]"} '
              'or {"found": false, "selector": null} if you could not find any element')
    response = call_llm(prompt)
    try:
        answer = json.loads(response.strip().removeprefix("```json").removesuffix("```").strip())
    except json.JSONDecodeError:
        logging.error(f"LLM returned non-JSON output: {response}")
        return None
    logging.info(f"LLM result: {answer}")
    return answer.get("selector") if answer.get("found") else None

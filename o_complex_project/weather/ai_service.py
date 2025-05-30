from openai import OpenAI
import os



def generate_fact(town):
    
    client = OpenAI(
        api_key=os.environ.get("AI_KEY"),
        base_url="https://api.proxyapi.ru/openai/v1",
    )

    response = client.responses.create(
        model="gpt-4o",
        tools=[{
            "type": "web_search_preview",
            "search_context_size": "low",
            "user_location": {
                "type": "approximate",
                "country": "RU",
                "city": f"{town}",
                "region": "Moscow"
            }
        }],
        input=f"Интересный факт про {town}. Напиши только факт и больше ничего."
    )
    for output_item in response.output:
        if output_item.type == "message":
            for content in output_item.content:
                if content.type == "output_text":
                    return content.text
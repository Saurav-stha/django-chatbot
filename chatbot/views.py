from django.shortcuts import render
from django.http import JsonResponse


# from openai import 

# client = OpenAI(
#     # This is the default and can be omitted
#     api_key=os.environ.get("OPENAI_API_KEY"),
# )

import openai

openai_api_key = 'in env gitignore'
openai.api_key = openai_api_key

#have to change model CODE 429(exceed current quota)
# maybe need premium plan
def ask_openai(message):
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        # prompt = message,
        messages = [
            {
                'role':'user',
                'content': message
            }
        ],
        max_tokens = 4096,
        n=1,
        stop = None,
        temperature = 0.7,
    )

    # print(response)
    answer = response.choices[0].message['content'].strip()

    return answer


def index(request):
    
    # return HttpResponse('yolooo')

    if request.method == 'POST':
        message = request.POST.get('message')
        response = ask_openai(message)
    
        context = {'message':message, 'response': response}
        return JsonResponse(context)
    
    return render(request, 'chatbot.html') 

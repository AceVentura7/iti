import openai
import os



openai.api_key = os.getenv('OPENAI_API_KEY')

def initial_response(city , num_days , likings , age , gender , budget , occupation , diet ):

    system_message = '''You are a travel agent who is goint to answer the user's requested itenary as they describe their criterions.

    Only create the following Structure for each day:
    Wake up Time - Time in AM/PM - not more than 1 line
    Line 1 - Things to do during the day based on the list of likings. Not more than 1-2 lines.
    Line 2 - Preffered mode of transport for the day.
    Line 3 - Ideal place to eat lunch and dinner based on the days itinerary and dietary preferences. 
    Line 4 - Any particular memorobilia that you should buy from the area.
    Line 5 - Things to do during the evening based on the list of likings. Not more than 1-2 lines.
    Line 6 - Noteworthy historic factoids or local events/beliefs/superstitions. 
    Line 7 - Noteworthy place to get a drink and also suggest the drink. Not more than 2 lines.
    Line 8 - Provide breakdown of the budget for the day.

    The overall, must fit within the budget of the person.'''

    user_input = f'''Hi I want to visit {city}, for {num_days} number of days. I am {gender} who is {age} years old and I am {diet}. I work as a {occupation}, and my budget for the trip is ${budget}. I like {likings}.'''

    messages = [
            {"role": "system", "content": f"{system_message}"},
            {"role": "user", "content": f"req: {user_input}"},
            {"role": "assistant", "content": f'Scope: '},

        ]
    return messages

    
        


def get_assistant_reply(messages):
    reply = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    return reply.choices[0]['message'].content






if __name__ == '__main__':
    city = input('City:    ')
    age = input('Age:   ')
    gender = input('Gender:   ')
    num_days = input('Number of days:    ')
    budget = input('Budget:   ')
    occupation = input('Occupation:    ')
    diet = input('Diet:   ')
    likings = input('List of likings separated by commas:    ')
    init = initial_response(city , num_days , likings , age , gender , budget , occupation , diet )
    some = get_assistant_reply(init)
    print(some)
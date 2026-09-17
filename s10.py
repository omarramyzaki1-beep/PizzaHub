# 1. Importing extensions
import streamlit as st
import google.generativeai as ai 

with st.sidebar:
    st.header('Chat with our AI Assistant✨')
    key = st.secrets['API']
    ai.configure(api_key=key)
    
    #selecting the model
    model = ai.GenerativeModel(model_name='gemini-3.5-flash')
    #taking user question
    question = st.chat_input('Ask anytthing..')
    #creating user chat message
    if question:
        with st.chat_message('user', avatar='😁'):
            st.write(question)
    # Adding AI assistant part


        #creating AI chat message
        with st.chat_message('ai', avatar='👨‍🍳'):
            with st.spinner('generating...🤖'):
                promt = f'''
                you are an ai assistant for italian pizza restaurant called PizzaHub.
                answer this question:
                {question}
                given that:
                working hours: 10AM to 11PM
                menu:
                1. Magerita Pizza: Small-140 EGP, Medium-180 E
GP, Large-200 EGP
                2. Chicken Ranch: Small-160 EGP, Medium-200 EGP, Large-250 EGP
                3. Pepperoni Pizza: Small-180 EGP, Medium-220 EGP, Large-300 EGP
                pasta:
                1. Spaghetti Bolognese: Small-120 EGP, Medium-160 EGP, Large-200 EGP
                2. Fettuccine Alfredo: Small-130 EGP, Medium-170 EGP, Large-210 EGP
                3. Penne Arrabbiata: Small-110 EGP, Medium-150 EGP, Large-190 EGP
                drinks:
                1. Coca-Cola: Small-20 EGP, Medium-30 EGP, Large-40 EGP
                orange juice: Small-25 EGP, Medium-35 EGP, Large-45 EGP
                3. Lemonade: Small-15 EGP, Medium-25 EGP, Large-35 EGP
                You are the official smart AI assistant for PizzaHub, an Italian restaurant specializing in pizza, pasta, and drinks.

Your job is to help customers choose the best food and drinks based on their preferences, questions, and budget.

You can:

* Answer questions about the menu.
* Tell customers the prices of food and drinks.
* Recommend the best options based on a customer's budget.
* Compare different menu items.
* Suggest the most expensive or best-value combination that fits within the customer's budget.
* Suggest multiple possible options when available.
* Calculate the total price of combinations.
* Tell customers how much money they will have left.

IMPORTANT RULES:

1. Only recommend items that exist on the PizzaHub menu below.
2. Never invent food, drinks, prices, discounts, ingredients, or services.
3. Always make sure the total price of a recommendation does not exceed the customer's budget.
4. When a customer tells you their budget, carefully calculate which items or combinations they can afford.
5. Try to give the customer the best value for their money.
6. If multiple combinations fit the budget, give 2–4 good options.
7. Clearly show the price of every recommended option and the total price.
8. When possible, tell the customer how much money will remain.
9. If the customer asks for "the best thing", explain that the recommendation is based on the available menu and their budget.
10. Be friendly, helpful, and enthusiastic.
11. use more emojies. 

WORKING HOURS:
PizzaHub is open every day from 10:00 AM to 11:00 PM.

====================
🍕 PIZZAS
=========

Margherita Pizza:

* Small: 140 EGP
* Medium: 180 EGP
* Large: 200 EGP

Chicken Ranch:

* Small: 170 EGP
* Medium: 200 EGP
* Large: 230 EGP

Pepperoni Pizza:

* Small: 180 EGP
* Medium: 220 EGP
* Large: 250 EGP

====================
🍝 PASTA
========

Spaghetti Bolognese:

* Small: 120 EGP
* Medium: 160 EGP
* Large: 200 EGP

Fettuccine Alfredo:

* Small: 130 EGP
* Medium: 170 EGP
* Large: 210 EGP

Penne Arrabbiata:

* Small: 110 EGP
* Medium: 150 EGP
* Large: 190 EGP

====================
🥤 DRINKS
=========

Coca-Cola:

* Small: 20 EGP
* Medium: 30 EGP
* Large: 40 EGP

Sprite:

* Small: 20 EGP
* Medium: 30 EGP
* Large: 40 EGP

Orange Juice:

* Small: 25 EGP
* Medium: 35 EGP
* Large: 45 EGP

====================
HOW TO HANDLE BUDGET QUESTIONS
==============================

If the customer says something like:
"I have 200 EGP, what should I get?"

You should:

1. Check all menu items and combinations.
2. Find good options that cost 200 EGP or less.
3. Prefer combinations that give good value and use the budget efficiently.
4. Suggest 2–4 options if possible.
5. Show the total price for each option.
6. Show how much money is left.

Example:

Customer:
"I have 200 EGP, what can I get?"

Assistant:
"With 200 EGP, here are some great options:

🍕 Option 1: Margherita Pizza Large — 200 EGP
💰 Money left: 0 EGP

🍝 Option 2: Spaghetti Bolognese Large — 200 EGP
💰 Money left: 0 EGP

🥤 Option 3: Fettuccine Alfredo Small + Coca-Cola Large
Total: 170 EGP
💰 Money left: 30 EGP

My recommendation: Margherita Pizza Large if you want pizza, or Spaghetti Bolognese Large if you prefer pasta! 😋"

====================
CUSTOMER QUESTION
=================

{question}

Answer the customer's question using only the PizzaHub information above.


                '''
                answer = model.generate_content(promt)
            
            st.write(answer.text)


# 2. App title & caption
st.title(':shimmer[:red[Welcome to PizzaHub]]🍕', 
    text_alignment='center') 
st.subheader('The best Italian restuarant serving pizza & pasta!')

# 3. Creating app tabs
pizza_tab, pasta_tab, drinks_tab = st.tabs(
    ['Pizzas🍕', 'Pasta🍝', 'Drinks🍹'])

# 4. Building pizza tab
with pizza_tab:
    col1, col2, col3 = st.columns(3)
    sizes = ['Small', 'Medium', 'Large']
    
    with col1:
        # Adding pizza image and name
        st.image('https://www.papajohnsegypt.com/images/Products/product_50_1768290827.jpg')
        st.subheader('Magerita Pizza', text_alignment='center')
        
        # Adding the size option
        margerita_size = st.segmented_control('Size:', 
            options=sizes, key=1, default='Medium')
        
        # Margerita prices
        margerita_prices = {
            'Small':140,
            'Medium':180,
            'Large':200
        }
        # Displaying the price
        margerita_price = margerita_prices[margerita_size]
        st.write(f'Price: :red[**{margerita_price}**] EGP')
        
        # Selecting the quantity
        margerita_qty = st.number_input('Choose quantity:',
                min_value=0, max_value=100, key='mrg_qty')
        
    with col2:
        # Adding pizza image and name
        st.image('https://www.papajohnsegypt.com/images/Products/Chicken-Ranch---Spicy-Korean.jpg')
        st.subheader('Chicken Ranch', text_alignment='center')
        
        # Adding the size option
        ranch_size = st.segmented_control('Size:', 
                    options=sizes, key=2, default='Medium')
        
        # Ranch prices
        ranch_prices = {
            'Small':170,
            'Medium':200,
            'Large':230
        }
        # Displaying the price
        ranch_price = ranch_prices[ranch_size]
        st.write(f'Price: :red[**{ranch_price}**] EGP')
        
        # Selecting the quantity
        ranch_qty = st.number_input('Choose quantity:',
                min_value=0, max_value=100, key='rch_qty')
    
    with col3:
        # Adding pizza image and name
        st.image('https://www.papajohnsegypt.com/images/Products/product_9_1768291533.jpg')
        st.subheader('Pepperoni Pizza', text_alignment='center')
        
        # Adding the size option
        pepperoni_size = st.segmented_control('Size:', 
                    options=sizes, key=3, default='Medium')
        
        # Pepperoni prices
        pepperoni_prices = {
            'Small':180,
            'Medium':220,
            'Large':250
        }
        # Displaying the price
        pepperoni_price = pepperoni_prices[pepperoni_size]
        st.write(f'Price: :red[**{pepperoni_price}**] EGP')
        
        # Selecting the quantity
        pepperoni_qty = st.number_input('Choose quantity:',
                min_value=0, max_value=100, key='ppr_qty')
    with pasta_tab:
        col1, col2, col3 = st.columns(3)
        sizes = ['Small', 'Medium', 'Large']
        with col1:
            # Adding pasta image and name
            st.image('https://newmansown.com/wp-content/uploads/2022/03/Hamburger-Pasta-Bake.jpg')
            st.subheader('Spaghetti Bolognese', text_alignment='center')
            
            # Adding the size option
            spaghetti_size = st.segmented_control('Size:', 
                options=sizes, key=4, default='Medium')
            
            # Spaghetti prices
            spaghetti_prices = {
                'Small':120,
                'Medium':160,
                'Large':200
            }
            # Displaying the price
            spaghetti_price = spaghetti_prices[spaghetti_size]
            st.write(f'Price: :red[**{spaghetti_price}**] EGP')
            
            # Selecting the quantity
            spaghetti_qty = st.number_input('Choose quantity:',
                    min_value=0, max_value=100, key='spg_qty')
            with col2:
                # Adding pasta image and name
                st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRfJHmNF8-tY-AooIO63b7gu9NEzcMfxEbEFysIsbMmRrbzf-PfvPxBIdt8&s=10')
                st.subheader('Fettuccine Alfredo', text_alignment='center')
                
                # Adding the size option
                fettuccine_size = st.segmented_control('Size:', 
                    options=sizes, key=5, default='Medium')
                
                # Fettuccine prices
                fettuccine_prices = {
                    'Small':130,
                    'Medium':170,
                    'Large':210
                }
                # Displaying the price
                fettuccine_price = fettuccine_prices[fettuccine_size]
                st.write(f'Price: :red[**{fettuccine_price}**] EGP')
                
                # Selecting the quantity
                fettuccine_qty = st.number_input('Choose quantity:',
                        min_value=0, max_value=100, key='ftt_qty')
                with col3:
                    # Adding pasta image and name
                    st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR2YZMfFuZ9x3k8z2E95j1617-a9GthXb8kF-XgUZWFKmVh6uuVFmSArec&s=10')
                    st.subheader('Penne Arrabbiata', text_alignment='center')
                    
                    # Adding the size option
                    penne_size = st.segmented_control('Size:', 
                        options=sizes, key=6, default='Medium')
                    
                    # Penne prices
                    penne_prices = {
                        'Small':110,
                        'Medium':150,
                        'Large':190
                    }
                    # Displaying the price
                    penne_price = penne_prices[penne_size]
                    st.write(f'Price: :red[**{penne_price}**] EGP')
                    
                    # Selecting the quantity
                    penne_qty = st.number_input('Choose quantity:',
                            min_value=0, max_value=100, key='pnn_qty')
    with drinks_tab:
        col1, col2, col3 = st.columns(3)
        sizes = ['Small', 'Medium', 'Large']
        with col1:
            # Adding drink image and name
            st.image('https://images.unsplash.com/photo-1554866585-cd94860890b7?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8Y29sYXxlbnwwfHwwfHx8MA%3D%3D')
            st.subheader('Coca-Cola', text_alignment='center')
            
            # Adding the size option
            coca_cola_size = st.segmented_control('Size:',
                options=sizes, key='cc_size', default='Medium') or 'Medium'
            
            # Coca-Cola prices
            coca_cola_prices = {
                'Small':20,
                'Medium':30,
                'Large':40
            }
            # Displaying the price
            coca_cola_price = coca_cola_prices[coca_cola_size]
            st.write(f'Price: :red[**{coca_cola_price}**] EGP')
            
            # Selecting the quantity
            coca_cola_qty = st.number_input('Choose quantity:',
                    min_value=0, max_value=100, key='cc_qty')
            with col2:
                # Adding drink image and name
                st.image('https://images.unsplash.com/photo-1680404005217-a441afdefe83?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8c3ByaXRlfGVufDB8fDB8fHww')
                st.subheader('Sprite', text_alignment='center')
                
                # Adding the size option
                sprite_size = st.segmented_control('Size:',
                    options=sizes, key='spr_size', default='Medium') or 'Medium'
                
                # Sprite prices
                sprite_prices = {
                    'Small':20,
                    'Medium':30,
                    'Large':40
                }
                # Displaying the price
                sprite_price = sprite_prices[sprite_size]
                st.write(f'Price: :red[**{sprite_price}**] EGP')
                
                # Selecting the quantity
                sprite_qty = st.number_input('Choose quantity:',
                        min_value=0, max_value=100, key='spr_qty')
                with col3:
                    # Adding drink image and name
                    st.image('https://images.unsplash.com/photo-1600271886742-f049cd451bba?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8b3JhbmdlJTIwanVpY2V8ZW58MHx8MHx8fDA%3D')
                    st.subheader('Orange Juice', text_alignment='center')
                    
                    # Adding the size option
                    orange_juice_size = st.segmented_control('Size:',
                        options=sizes, key='oj_size', default='Medium') or 'Medium'
                    
                    # Orange Juice prices
                    orange_juice_prices = {
                        'Small':25,
                        'Medium':35,
                        'Large':45
                    }
                    # Displaying the price
                    orange_juice_price = orange_juice_prices[orange_juice_size]
                    st.write(f'Price: :red[**{orange_juice_price}**] EGP')
                    
                    # Selecting the quantity
                    orange_juice_qty = st.number_input('Choose quantity:',
                            min_value=0, max_value=100, key='oj_qty')
    st.divider()
    total = (
        (margerita_price * margerita_qty) +
        (ranch_price * ranch_qty) +
        (pepperoni_price * pepperoni_qty) +
        (spaghetti_price * spaghetti_qty) +
        (fettuccine_price * fettuccine_qty) +
        (penne_price * penne_qty) +
        (coca_cola_price * coca_cola_qty) +
        (sprite_price * sprite_qty) +
        (orange_juice_price * orange_juice_qty)
    )

    if st.button('calculate total 💸', 
                 use_container_width=True, type='primary') == True:
        st.subheader('🛒 order summary')
        order_summary = [
                        ['item', 'quantity', 'total price'], 
                        ['Magerita Pizza', margerita_qty, margerita_price * margerita_qty],
                        ['Chicken Ranch', ranch_qty, ranch_price * ranch_qty],
                        ['Pepperoni Pizza', pepperoni_qty, pepperoni_price * pepperoni_qty],
                        ['Spaghetti Bolognese', spaghetti_qty, spaghetti_price * spaghetti_qty],
                        ['Fettuccine Alfredo', fettuccine_qty, fettuccine_price * fettuccine_qty],
                        ['Penne Arrabbiata', penne_qty, penne_price * penne_qty],
                        ['Coca-Cola', coca_cola_qty, coca_cola_price * coca_cola_qty],
                        ['Sprite', sprite_qty, sprite_price * sprite_qty],
                        ['Orange Juice', orange_juice_qty, orange_juice_price * orange_juice_qty]
                    ]
        st.table(order_summary)
        
                    
        

        
        
        st.subheader(f'Total: :green[**{total}**] EGP')

        st.toast('Total calculated successfully!', icon='✅', duration=3)

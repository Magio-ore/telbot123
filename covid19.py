


@bot.message_handler(content_types=['text'])
def mess(message):
    final_message = ""
    get_message_bot = message.text.strip().lower()
if get_message_bot == "😱 Статистика Covid-19":
    location = covid19.getLocationByCountryCode("UA")
    if final_message == "":
       date = location[0]['last_updated'].split("T")
       time = date[1].split(".")
       final_message = f"<u>Дані по країні:</u>\nНаселення: {location[0]['country_population']}"
       f"Останнє оновлення: {date[0]}{tiem[0]}\n"
       f"Захворівших: </b>{location[0]['latest']['confirmed']:,}\n<b>Смерті: {location[0]['latest']['deaths']:,}"
bot.send_message(message.chat.id, final_message, parse_mode='html')

# latest = covid19.getLatest()
# location = covid19.getLocationByCountryCode("UA")

def weatherlviv(message):
    r = requests.get('https://ua.sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%BB%D1%8C%D0%B2%D1%96%D0%B2')
    html = BS(r.content, 'html.parser')

    for el in html.select('#content'):
        t_min = el.select('.temperature .min')[0].text
        t_max = el.select('.temperature .max')[0].text
        text = el.select('.wDescription .description')[0].text

    if call.message:
       if call.data == 'weatherlv':
          bot.send_message(call.message.chat.id, "Пивіт погода сьогодні у м.Львові:\n" +
                     t_min + ', ' + t_max + '\n' + text, reply_markup=markup)

def weatherostriv(message):
    r = requests.get('https://ua.sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%BE%D1%81%D1%82%D1%80%D1%96%D0%B2-303019575')
    html = BS(r.content, 'html.parser')

    for el in html.select('#content'):
        t_min = el.select('.temperature .min')[0].text
        t_max = el.select('.temperature .max')[0].text
        text = el.select('.wDescription .description')[0].text

    if call.message:
       if call.data == 'weatherostriv':
          bot.send_message(message.chat.id, "Пивіт погода сьогодні у с.Острів:\n" +
                     t_min + ', ' + t_max + '\n' + text, reply_markup=markup)

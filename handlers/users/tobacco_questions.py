from aiogram import types

from loader import dp


@dp.message_handler(commands=['about_marking'])
async def work_process(message: types.Message):
    await message.reply("Что такое (ИС МОТП)? "
                        "ИС МОТП - информационная система маркировки и оборота табачной продукции.\n\n"
                        "Что такое система маркировки? Для чего она вводится в России?\n"
                        "Проблема нелегальной продукции остается крайне острой для России: доля незаконного оборота в"
                        " легкой промышленности достигает 35%, на парфюмерном рынке 20%, на рынке лекарственных"
                        "средств до 10%.\n\n"
                        "В первом квартале 2018 года доля нелегального рынка сигарет в России увеличилась до 7,7% "
                        "против"
                        " 4,6% годом ранее, следует из исследования аналитического агентства Kantar TNS."
                        "В декабре 2017 г. Президент РФ В.Путин одобрил решение правительства о создании до 2024 г. "
                        "национальной системы цифровой маркировки товаров на базе Центра развития перспективных "
                        "технологий (ЦРПТ)."
                        "ЦРПТ является совместным проектом ЮСМ («ЮэСэМ Технологии», 50%), госкорпорации Ростех "
                        "(концерн «Автоматика», 25%) и «Элвис-Плюс групп» (25%)."
                        "Создаваемая центром система, получившая название Честный ЗНАК, позволяет эффективно бороться "
                        "с контрафактом и контрабандой, защищает легальный бизнес, бренд добросовестного производителя "
                        "и потребителей."
                        "Единая система цифровой маркировки позволит бизнесу повысить производительность, "
                        "совершенствовать логистические схемы, нарастить долю рынка и в конечном счете "
                        "увеличить выручку:\n"
                        "за счет снижения доли контрабанды и контрафакта легальные производители увеличат долю и "
                        "объемы производства на 5-50% в зависимости от товарной группы;\n"
                        "бизнес сможет перевести производство на Индустрию 4.0, на работу по принципу Just-in-Time. "
                        "Получая в режиме онлайн данные о движении продукции, он будет оптимально планировать "
                        "производство, снижать запасы и повышать оборачиваемость продукции;\n"
                        "бизнес сможет существенно экономить на логистике: при внедрении полного прослеживания "
                        "получение производителем или логистической компанией актуального статистического материала "
                        "о географии, интенсивности, сезонности продаж позволит перестроить логистические схемы, "
                        "оптимизировать поставки и складские запасы;\n"
                        "бизнес наладит учет. Сейчас многие предприниматели не имеют собственных данных об "
                        "остатках и кодах товаров на складах и в магазинах. Без правильного учета невозможно считать "
                        "прибыль или планировать закупки, поэтому автоматизация поможет предпринимателям навести "
                        "порядок в своем бизнесе;\n"
                        "бизнес перейдет на электронный документооборот. ЭДО радикально сокращает объем бумажных "
                        "документов, которыми до сих пор активно обмениваются между собой российские компании и "
                        "снизит издержки бизнеса и повысит производительность труда.\n\n"
                        "Кто и когда принял решение о введении маркировки табачной продукции в России? Какие "
                        "государственные органы будут курировать эту систему?\n"
                        "В соответствии с постановлением Правительства Российской Федерации от 27 ноября 2017 г. "
                        "№ 1433 «О проведении эксперимента по маркировке табачной продукции средствами идентификации и "
                        "мониторингу оборота табачной продукции» с 15 января 2018 г. на территории Российской "
                        "Федерации "
                        "проводится эксперимент, координацию которого осуществляет Минпромторг России.\n\n"
                        "С 1 марта 2019 года цифровая маркировка стала обязательной для табачной отрасли. Внесенные в "
                        "ФЗ-15 изменения, утверждающие срок 1 марта 2019 г. как старт обязательной маркировки, "
                        "подписаны "
                        "президентом РФ В.Путиным 30 июля 2018 года.\n\n"
                        "Каковы сроки введения обязательной маркировки табака?\n"
                        "С 1 марта 2019 года началась обязательная регистрация производителей и торговых точек в "
                        "Национальной системе цифровой маркировки Честный ЗНАК.\n"
                        "для регистрации в системе маркировки необходимо оставить заявку на странице Маркировки "
                        "табака.\n"
                        "С 1 июля 2019 года будет прекращен выпуск немаркированной продукции.\n\n"
                        "при продаже сигарет на кассе нужно просканировать DataMatrix код с каждой пачки или блока. "
                        "При продаже товара касса должна передать в ОФД информацию о том, что в чеке содержится "
                        "маркируемая продукция;\n"
                        "поставка маркированных сигарет дистрибьютору, напрямую от производителя, будет сопровождаться "
                        "электронными универсальными передаточными документами (УПД) с указанием кодов продукции при "
                        "помощи систем электронного документооборота.\n\n"
                        "С 1 июля 2020 года будет прекращен оборота немаркированной продукции."
                        "поставка маркированных сигарет в розничную точку и субдистрибьютору будет сопровождаться "
                        "электронными универсальными передаточными документами (УПД) с указанием кодов продукции при "
                        "помощи систем электронного документооборота.\n\n"
                        "С какого числа организации и индивидуальные предприниматели, осуществляющие розничную "
                        "торговлю табачной продукции, должны:"
                        "— отправлять данные о розничной продаже табачной продукции в систему мониторинга;"
                        "— отправлять данные о получении табачной продукции от поставщика в систему мониторинга;"
                        "— продавать исключительно маркированную табачную продукцию."
                        "Организации и индивидуальные предприниматели, осуществляющие розничную торговлю табачной "
                        "продукции, должны передавать в информационную систему мониторинга:"
                        "с 1 июля 2019 г. сведения о розничной продаже маркированной табачной продукции "
                        "(сигарет и папирос), произведенной в Российской Федерации или ввезенной в Российскую "
                        "Федерацию;"
                        "с 1 июля 2020 г. сведения о получении табачной продукции от поставщиков, а также о других "
                        "операциях с табачной продукции, включая информацию о ее списании по основаниям, установленным "
                        "законодательством.\n"
                        "Розничная продажа немаркированной табачной продукции, включая сигареты и папиросы, "
                        "произведенной в Российской Федерации или ввезенной в Российскую Федерацию после до 1 июля "
                        "2019 г., может беспрепятственно осуществляться до 1 июля 2020 г."
                        "С 1 июля 2020 г. допускается розничная продажа только маркированной табачной продукции.\n"
                        "Каким образом розница в отдаленных местностях будет передавать данные в систему маркировки?"
                        "Предпринимателям, которые используют кассы без передачи данных в ОФД, будет необходимо 1 раз "
                        "в 30 дней вносить данные о кодах проданных пачек в личный кабинет системы мониторинга.\n"
                        "Что такое пилотный проект, для чего он нужен?"
                        "Перед переходом к обязательной маркировке в каждой товарной группе проводятся пилотные "
                        "проекты."
                        " Они необходимы для того, чтобы представители отрасли смогли в спокойном режиме вместе с "
                        "оператором проекта подготовиться к работе с маркированной продукцией: адаптировать "
                        "оборудование"
                        " для печати кодов, обновить кассовое ПО и тд.\n\n"
                        "Именно пилотные проекты, которые должны начинаться не позднее, чем за год до начала "
                        "обязательной маркировки позволяют отрасли подготовиться к ней и минимизировать издержки.\n\n"
                        "Будет ли взиматься какая-то плата за генерацию кодов с участников пилотного проекта?"
                        " Что такое "
                        "(ИС МОТП)?"
                        "На этапе пилотного проекта все участники получат доступ к системе, включая генерацию цифровых"
                        " кодов маркировки и прослеживаемость их оборота, на безвозмездной основе."
                        "Кто принимал участие в пилотном проекте по маркировке табака?"
                        "Участниками эксперимента были производители табачной продукции в России, выпускающие около "
                        "95% всей табачной продукции в стране – «Japan Tobacco International», "
                        "«Philip Morris International», «British American Tobacco», «Imperial Tobacco», "
                        "«Донской табак», «Korea Tomorrow & Global Corporation», «Union Tobacco Factory»); "
                        "дистрибьюторы, через которых реализуется более 88% табачной продукции – ТК «Мегаполис», "
                        "ГК «СНС»; организации розничной торговли – «X5 Retail Group», «Metro C&C», «Лента», «Магнит»,"
                        " «Дикси» и др."
                        "Что изменится в работе каждого участника рынка после перехода на работу с маркированными "
                        "табачными пачками?"
                        "Для участников рынка изменения будут минимальными."
                        "Производителям нужно настроить процесс нанесения цифрового кода Data Matrix "
                        "на пачках и блоках "
                        "и линейного кода на коробах. Нанесенный на каждую единицу товара цифровой код будет "
                        "сканироваться участниками торговой цепи. Информация о его передвижении будет передаваться в "
                        "систему Честный ЗНАК."
                        "Дистрибьюторы будут передавать сведения в систему маркировки в электронном виде через "
                        "операторов электронного документооборота посредством универсального передаточного документа "
                        "(УПД), который включает в себя товарную накладную и счет-фактуру. Данный документ разработан "
                        "ФНС России и рекомендован к применению. Для тех, кто еще не перешел к работе с ЭДО, нужно "
                        "будет это сделать."
                        "После поступления товара в розницу при его реализации будет необходимо передавать информацию "
                        "о продаже в систему маркировки Честный ЗНАК. Для этого на кассе нужно будет просканировать "
                        "код с пачки, который будет автоматически передан в Честный ЗНАК через оператора фискальных "
                        "данных, к которому подключена касса. За счет того, что в коде содержится GTIN продукции – "
                        "достаточно просканировать только сам Data Matrix. Благодаря тому, что в системе уже содержатся"
                        " данные о максимальной розничной цене, кассиру не придется вводить эту информацию на кассе."
                        "Для розничных магазинов рекомендуется прочитать подробную информацию в разделе «Подготовка "
                        "магазина к маркировке»."
                        "Напомним, что с 1 июля 2019 года все торговые точки будут оборудованы онлайн-кассами по "
                        "требованиям 54-ФЗ и устанавливать дополнительное программное и аппаратное обеспечение как в "
                        "ЕГАИС не потребуется. Расходы продавцов на адаптацию процессов для маркировки будут "
                        "минимальными.\n\n"
                        "Ресурсы и оборудование, необходимые для внедрения системы маркировки и прослеживаемости "
                        "табачной продукции:"
                        "Для работы с системой потребуется следующее техническое оборудование:"
                        "Производителям:"
                        "оборудование и ПО для сериализации и агрегации (если ранее не приобреталось);"
                        "регистраторы эмиссии кодов маркировки (оператором проекта Центр развития перспективных "
                        "технологий предоставляет их бесплатно);"
                        "подключение к оператору электронного документооборота (если в ЭДО ранее не работали)."
                        "Дистрибьюторам и оптовикам:"
                        "подключение к оператору электронного документооборота (ЭДО) и цифровая подпись "
                        "(если ранее не оформлялось)."
                        "Розничной точке:"
                        "2D сканер (если ранее он не закупался) и обновление программного обеспечения для "
                        "уже установленной онлайн-кассы;"
                        "для розничных магазинов рекомендуется прочитать подробную информацию в разделе "
                        "«Подготовка магазина к маркировке»;"
                        "Необходимые затраты для внедрения маркировки и прослеживаемости для разных групп "
                        "участников рынка единовременные и постоянные:"
                        "Для производителей:"
                        "в случае отсутствия необходимого оборудования и ПО, производителям потребуется "
                        "единоразово вложить от 6 до 15 млн рублей на производственную линию для его покупки "
                        "и адаптации в зависимости от выбранной системы ERP;"
                        "регистратор эмиссии предоставляет ЦРПТ на бесплатной основе;"
                        "для оптовой продажи необходимо использование ЭДО для отправки первичных документов. "
                        "Средний рыночный тариф за обработку одного документа в ЭДО - 5,4 руб. Средние годовые "
                        "расходы на услуги ЭДО составят порядка 21 млн. руб. для крупных производителей и"
                        " 0,7 для мелких."
                        "Для дистрибьюторов и оптовиков:"
                        "В зависимости от масштаба бизнеса дистрибьютора или оптовика расходы за услуги ЭДО "
                        "в год могут варьироваться (ниже приведена примерная оценка, исходя из среднего рыночного "
                        "тарифа за обработку одного документа в ЭДО - 5,4 руб.):"
                        "у оптовиков с оборотом в 50 млн. пачек в год расходы на ЭДО будут составлять до 270 тыс. "
                        "рублей в год;"
                        "у дистрибьютеров с оборотом в 9 млрд. пачек в год расходы на ЭДО будут составлять до 49 млн"
                        " рублей в год;"
                        "у оптовиков с оборотом в 3 млрд. пачек в год расходы на ЭДО будут составлять до 15 млн рублей "
                        "в год;"
                        "у оптовиков с оборотом в 1 млрд. пачек в год расходы на ЭДО будут составлять до 5 млн рублей "
                        "в год;"
                        "входящий трафик электронных документов не тарифицируется."
                        "Для розничных магазинов:"
                        "в случае отсутствия у продавца 2D сканера будет необходимо единоразово инвестировать "
                        "4000 рублей в его приобретение;"
                        "для мелкой розницы может потребоваться установка обновленного кассового ПО для работы"
                        " с маркированной продукцией. Поддержка кассового ПО – 7500/год. Данную информацию можно "
                        "уточнить в сервисных центрах поставщиков кассового оборудования."
                        "Необходимо отметить, что затраты на ЭДО окупаются за счет сокращения оборота бумажных "
                        "документов и, следовательно, сокращения затрат связанных с печатью, пересылкой и хранением "
                        "бумажных документов. Средняя стоимость бумажного документа составляет 20 рублей, что в 4 раза "
                        "больше, чем стоимость электронного документа.\n\n"
                        "Я разработчик ПО и у меня есть предложение для оператора системы маркировки. Куда я могу"
                        " обратиться?\n"
                        "Да мы приглашаем к участию в проекте разработчиков решений, интеграторов и хотим сделать "
                        "нашу систему максимально открытой, удобной и полезной для рынка. Направьте Ваши предложения "
                        "на support@crpt.ru.\n"
                        "Горячая линия для обращения участников рынка с вопросами по системе маркировки и "
                        "прослеживаемости табачной продукции.\n"
                        "8 800 222 1523 (для звонков из России)\n"
                        "+7 499 350 85 59 (для звонков из других стран)\n"
                        "support@crpt.ru'")


@dp.message_handler(commands=['liability_and_fines'])
async def for_whom(message: types.Message):
    await message.reply(
        'Какую ответственность будут нести розничные магазины в случае неправильного использования контрольно-кассовой '
        'техники?\n'
        'Согласно федеральному закону № 54-ФЗ о применении контрольно-кассовой техники (статья 4.7 п. 5) Правительство '
        'Российской Федерации вправе устанавливать дополнительный обязательный реквизит кассового чека — «код товара», '
        'позволяющий идентифицировать товар.'
        'Постановлением Правительства РФ № 174 от 21 февраля 2019 года установлено, что в реквизите «код товара» '
        'кассового чека для товаров, в отношении которых предусмотрена обязательная маркировка средствами '
        'идентификации, указывается код идентификации, предусмотренный Федеральным законом от 28.12.2009 № 381-ФЗ '
        '«Об основах государственного регулирования торговой деятельности в Российской Федерации».'
        'За несоблюдение этого требования, может быть применена ответственность, которая установлена частью 4'
        ' статьи 14.5 КоАП РФ за нарушение порядка и условий применения кассовой техники, в виде предупреждения или '
        'наложения административного штрафа на должностных лиц в размере от полутора тысяч до трех тысяч рублей; на'
        ' юридических лиц — в виде предупреждения или наложения административного штрафа в размере от пяти тысяч до '
        'десяти тысяч рублей.\n\n'
        'Какую ответственность будут нести те, кто будет продавать маркированную продукцию после 1 июля 2019 года '
        'без передачи сведений в систему маркировки?\n'
        'Какую ответственность будут нести те, кто будет продавать немаркированную продукцию после 1 июля 2020 года?\n'
        'Согласно постановлению правительства № 224 от 28 февраля 2019 года утверждены правила маркировки и оборота '
        'табачной продукции.'
        'Согласно правилам с 01 июля 2019 года за продажу немаркированных сигарет, произведенных после 1 июля 2019 г. '
        'предусмотрена ответственность в соответствии со статьей 15.12 Кодекса РФ об административных правонарушениях:'
        'на граждан в размере от двух тысяч до четырех тысяч рублей с конфискацией предметов административного '
        'правонарушения;'
        'на юридических лиц — от пятидесяти тысяч до трехсот тысяч рублей с конфискацией предметов административного '
        'правонарушения'
        'на должностных лиц — от пяти тысяч до десяти тысяч рублей с конфискацией предметов административного '
        'правонарушения;\n'
        'Немаркированные остатки, произведенные до 1 июля 2019 года, могут продаваться беспрепятственно до 1 июля '
        '2020 года. С этой даты ответственность за продажу немаркированных сигарет наступает в полном объеме.\n\n'
        'Какую ответственность будут нести производители табачной продукции за производство немаркированных сигарет '
        'после 1 июля 2019 года?\n'
        'Ответственность за производство немаркированной продукции предусмотрена статьей 15.12 Кодекса РФ об '
        'административных правонарушениях.'
        'Производство алкогольной продукции или табачных изделий без маркировки и (или) нанесения информации, '
        'предусмотренной законодательством Российской Федерации, а также с нарушением установленного порядка '
        'соответствующей маркировки и (или) нанесения информации — влечет наложение административного штрафа на '
        'должностных лиц в размере от десяти тысяч до пятнадцати тысяч рублей с конфискацией предметов '
        'административного правонарушения; \n на юридических лиц — от ста тысяч до ста пятидесяти тысяч рублей с '
        'конфискацией предметов административного правонарушения.'
    )

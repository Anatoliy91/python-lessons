def post_default_request(url, data, headers):
    # метод делает пост запрос и возвращает полностью весь респонс
    return response


def default_dict_to_json(di):
    # этот метод превращает дикт в Джейсон. Возвращает джецсон
    return json_data


def default_json_to_dict(json):
    # этот метод парсит Джейсон и возвращает дикт
    dict_data = json.loads(r.text)
    return dict_data


def get_headers(env):
    # метод в зависимости от енвайрмента возвращает нужные хедеры
    return headers


def get_random_password():
    # возвращает рандомные пароль
    return password


def get_random_email():
    # возвращает рандомны емейл
    return email


def det_baseurl('env'):
    # возвращает базовую урлу в зависимости от энвайрмента
    return baseurl


def test_check_resp():
    body = {

    }
    body_json = default_json_to_dict(body)
    headers = get_headers('stg')
    headrrs_json = default_json_to_dict(headers)
    url = get_baseurl('stg') + "метод"
    resp = post_default_request(url=url, data=body_json, headers=headers_json)
    text_data = default_json_to_dict(resp)
# дальше проверки



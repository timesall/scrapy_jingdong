from django.shortcuts import render
from jdshow.models import mobile
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from decimal import Decimal
import re
# Create your views here.


def index(request):
    items = mobile.objects[:50]  # 取50条数据,列表
    # 用于echat数据
    price_list = []
    phone_name = []
    for i in items:
        price_list.append(i['product_price'])
        name = i['product_name'].replace('\n', '').replace(' ', '')[:10]
        # reg = re.compile(r'(.*?)版$', re.S)  # \u7248
        # new_name = reg.match(name).group(1)
        phone_name.append(name)
        # print(name.encode('utf-8'))
    # print(price_list)

    paginator = Paginator(items, 10, 2)  # 实例化结果集,每页十条数据,少于两页则合并到上一页中
    page = request.GET.get('page')
    try:
        rows = paginator.page(page)
    except PageNotAnInteger:
        rows = paginator.page(1)  # 如果输入的不是整数就显示第一页
    except EmptyPage:
        rows = paginator.page(paginator.num_pages)  # 如果是空的就展示最后一页

    return render(request, 'jdshow/index.html', {'items': rows, 'prices': price_list, 'names': phone_name})


def phone_info(request, product_id):
    # 根据product_id找到商品的各个属性
    items = mobile.objects(product_id=product_id)
    url = 'https:' + items.first().product_url
    good_count = items.first().good_comment  # 好评数量
    gen_count = items.first().gen_comment  # 中评数量
    bad_count = items.first().bad_comment  # 差评数量
    comment_count = items.first().all_comment
    good_comment_rate = round(Decimal(good_count) / int(comment_count))
    bad_comment_rate = round(Decimal(good_count) / int(bad_count))
    gen_comment_rate = round(Decimal(good_count) / int(gen_count))
    data = {'good_rate': good_comment_rate, 'url': url, 'comment_num': comment_count,
            'bad_rate': bad_comment_rate, 'gen_rate': gen_comment_rate,
            'good': good_count, 'bad': bad_count, 'gen': gen_count}
    return render(request, 'jdshow/phone_info.html', {"items": items, "data": data})


# 注册及登录
def reg_login(request):
    return render(request, 'jdshow/reg&login.html')
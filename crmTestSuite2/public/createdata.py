from crmTestSuite2.public.crmdatabase import CRM_database
import random

def name():#姓名
    name= ''.join(
        [random.choice(["德菲", "日诚", "天真", "343534","展时邦", "洋迅洋创", "禾祥", "速美", "太丝", "优正方", "迈光贝迪", "众都", "傲纽", "辰南", "\
    希龙成", "慧瑞原联", "扬风", "火晶", "同亿", "高新禾", "智云贝奥", "诺熙", "久星", "双旺", "康祥康", "惠园伟信", "启辉", "诗奥", "诚湖", "妙凌迈", "安诺贝德", \
                        "今致", "讯新", "卓禾","%#@#$%", "正复安","teat___", "亿锐立好"])])
    return name
def age():#年龄
    age= [str(random.randint(1, 99))]
    return age
def gender():#性别
    gender= ''.join([str(random.choice(["男", "女"]))])
    return gender
def edu():  #学历
    edu= ''.join([str(random.choice(["初中", "高中","本科","博士","硕士"]))])
    return edu
def department(): #随机部门
    db = CRM_database()
    all = db.excute('select department_name from department_info', 2)
    department=''.join(all[random.randint(0,len(all)-1)][0])
    return department
def landline(): #座机号
    landline=''.join([str(random.randint(1,9)) for i in range(8)]) #生成8位座机号
    return landline
def bank_card_number():#银行卡号
    bank_card_number=''.join([str(random.randint(1,9)) for i in range(18)])
    return bank_card_number
def id():#身份证
    ID = [str(random.randint(1, 9)) for i in range(5)]
    id = '5103111900030'+''.join(ID)
    return id
def tel():
    a = ''.join(str(random.choice([180, 139,155, 138, 153, 134, 135, 136, 137, 138])))
    tel_0 = [str(random.randint(0, 9)) for i in range(8)]
    tel=str(a)+''.join(tel_0)
    return tel
def addMan():
    addMan= ''.join([str(random.choice(["张三", "李四","王大锤","99999","TTTT@#$%"]))])
    return addMan
def user_num(): #账号
    a = ''.join(random.choice(['crm', 'emp','user',]))
    user_num_0 = [str(random.randint(0, 9)) for i in range(5)]
    user_num=str(a)+''.join(user_num_0)
    return user_num
def nation(): #民族
    nation=''.join([str(random.choice(["汉族", "TTTEEEESSSTTT","#￥%（*（））*（","99999","__TTTT@#$%"]))])
    return nation
def marriage(): #婚姻状况
    marriage= ''.join([str(random.choice(["已婚", "未婚", "离异"]))])
    return marriage
def role(): #随机角色
    db = CRM_database()
    all = db.excute('select role_name from user_role', 2)
    role=''.join(all[random.randint(0,len(all)-1)][0])
    return role
def faveriate():
    faveriate=''.join([str(random.choice(["v指定分隔符政府v敢死队风格发表", "TTTEEEESSSTTTEEEESSSTTTTTTEEEESSSTTTTTTEEEESSSTTTTTTEEEESSSTTTTTT", "#￥%（*（））*（", "999564534534545655675699", "__TTTT@#$%"]))])
    return faveriate
def dress():
    dress_1=[str(random.choice(["河北省","山西省","辽宁省","吉林省","黑龙江省","江苏省","浙江省","安徽省","福建省","江西省","山东省","河南省","湖北省","湖南省","广东省","海南省","四川省","贵州省","云南省","陕西省","甘肃省","青海省","台湾省","内蒙古自治区","广西壮族自治区","西藏自治区","宁夏回族自治区","新疆维吾尔自治区",
"北京市","天津市","上海市","重庆市","香港特别行政区","澳门特别行政区"]))]
    dress_2=[random.choice(["北京","上海","广州","深圳","成都","杭州","佛山","苏州","西安","天津","上海","北京","深圳","天津","苏州","重庆","杭州","武汉","广州","宁波","广州","北京","上海","南京","杭州","武汉","深圳","长沙","苏州","沈阳","北京","上海","深圳","广州","天津","杭州","苏州","南京","重庆","成都","天津","重庆","武汉","长沙","青岛","合肥","郑州","东营","无锡","南京"])]
    dress_3=[random.choice(["万州区","涪陵区","渝中区","大渡口区","江北区","沙坪坝区","九龙坡区","南岸区","北碚区","万盛区","双桥区","渝北区","巴南区","黔江区","长寿区","江津区","合川区","永川区","南川区綦江县","潼南县","铜梁县","大足县","荣昌县","璧山县","梁平县","城口县","丰都县","垫江县","武隆县","忠县","开县","云阳县","奉节县","巫山县","巫溪县","石柱土家族自治县","秀山土家族苗族自治县","酉阳土家族苗族自治县","彭水苗族土家族自治县"])]
    dress=''.join(dress_1)+"".join(dress_2)+"".join(dress_3)
    return dress

def email():
    email=(''.join([str(random.randint(0, 9)) for i in range(9)]))+''.join([str(random.choice(["@qq.com", "@163.com", "@sina.com"]))])
    return email



# db = CRM_database()
# all = db.excute('select role_name from user_role', 2)
# print(all)
# role=''.join(all[random.randint(0,len(all))][0])
# print(role)

email1=(''.join([str(random.randint(0, 9))])+''.join([str(random.randint(0, 9)) for i in range(9)]))+''.join([str(random.choice(["@qq.com", "@163.com", "@sina.com"]))])
print(email1)
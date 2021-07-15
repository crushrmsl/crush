import random
class Base:
    def rfid(self):
        # 随机生成rfid
        c = ''
        list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                 'v', 'w', 'x', 'y', 'z', 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        a = [random.choice(list1) for i in range(32)]
        for i in a:
            c += str(i)
        return c

    def usernum(self):
        # 随机生成账号
        o = ''
        list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                 'v', 'w', 'x', 'y', 'z', 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        a = [random.choice(list1) for i in range(6)]
        for i in a:
            o += str(i)
        return o

    def userpw(self):
        # 随机生成密码
        u = ''
        list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                 'v', 'w', 'x', 'y', 'z', 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        a = [random.choice(list1) for i in range(6)]
        for i in a:
            u += str(i)
        return u


    def phone(self):  # 随机生成手机号
        q = '157'
        w = [random.randint(0, 9) for i in range(8)]
        for j in w:
            q += str(j)
        return q


    def age(self):  # 随机生成年龄
        l = [str(random.randint(18, 50))]
        return l


    def idcard(self):  # 随机生成身份证号
        y = '51102319'
        p = [random.randint(70, 99) for i in range(1)]
        o = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        t = random.choice(o)
        u = [random.randint(10, 30) for i in range(3)]
        for j in p:
            y += str(j)
        y += str(t)
        for h in u:
            y += str(h)
        return y


    def zjphone(self):  # 随机生成座机号码
        t = '54'
        w = [random.randint(0, 9) for i in range(6)]
        for j in w:
            t += str(j)
        return t


    def bankid(self):  # 随机生成银行卡号
        t = str(random.randint(1, 9))
        w = [random.randint(0, 9) for i in range(18)]
        for j in w:
            t += str(j)
        return t


    def name(self):  # 随机生成姓名
        firstname = ['王', '李', '张', '刘', '陈', '杨', '黄', '赵', '吴', '周', '徐', '孙', '马', '朱', '胡', '郭', '何', '高', '林', '罗',
                   '郑', '梁', '谢', '宋', '唐', '位', '许', '韩', '冯', '邓', '曹', '彭', '曾', '萧', '田', '董', '潘', '袁', '于', '蒋',
                   '蔡', '余', '杜', '叶', '程', '苏', '魏', '吕', '丁', '任', '沈', '姚', '卢', '姜', '崔', '钟', '谭', '陆', '汪', '范',
                   '金', '石', '廖', '贾', '夏', '韦', '傅', '方', '白', '邹', '孟', '熊', '秦', '邱', '江', '尹', '薛', '阎', '段', '雷',
                   '侯', '龙', '史', '陶', '黎', '贺', '顾', '毛', '郝', '龚', '邵', '万', '钱', '严', '覃', '武', '戴', '莫', '孔', '向',
                   '汤']

        lastname = ['丹', '举', '义', '之', '乐', '书', '乾', '云', '亦', '从', '代', '以', '伟', '佑', '俊', '修', '健', '傲', '儿', '元', '光',
                '兰', '冬', '冰', '冷', '凌', '凝', '凡', '凯', '初', '力', '勤', '千', '卉', '半', '华', '南', '博', '又', '友', '同', '向',
                '君', '听', '和', '哲', '嘉', '国', '坚', '城', '夏', '夜', '天', '奇', '奥', '如', '妙', '子', '存', '季', '孤', '宇', '安',
                '宛', '宸', '寒', '寻', '尔', '尧', '山', '岚', '峻', '巧', '平', '幼', '康', '建', '开', '弘', '强', '彤', '彦', '彬', '彭',
                '心', '忆', '志', '念', '怀', '怜', '恨', '惜', '慕', '成', '擎', '敏', '文', '新', '旋', '旭', '昊', '明', '易', '昕', '映',
                '春', '昱', '晋', '晓', '晗', '晟', '景', '晴', '智', '曼', '朋', '朗', '杰', '松', '枫', '柏', '柔', '柳', '格', '桃', '梦',
                '楷', '槐', '正', '水', '沛', '波', '泽', '洁', '洋', '济', '浦', '浩', '海', '涛', '润', '涵', '渊', '源', '溥', '濮', '瀚',
                '灵', '灿', '炎', '烟', '烨', '然', '煊', '煜', '熙', '熠', '玉', '珊', '珍', '理', '琪', '琴', '瑜', '瑞', '瑶', '瑾', '璞',
                '痴', '皓', '盼', '真', '睿', '碧', '磊', '祥', '祺', '秉', '程', '立', '竹', '笑', '紫', '绍', '经', '绿', '群', '翠', '翰',
                '致', '航', '良', '芙', '芷', '苍', '苑', '若', '茂', '荣', '莲', '菡', '菱', '萱', '蓉', '蓝', '蕊', '蕾', '薇', '蝶', '觅',
                '访', '诚', '语', '谷', '豪', '赋', '超', '越', '轩', '辉', '达', '远', '邃', '醉', '金', '鑫', '锦', '问', '雁', '雅', '雨',
                '雪', '霖', '霜', '露', '青', '靖', '静', '风', '飞', '香', '驰', '骞', '高', '鸿', '鹏', '鹤', '黎']
        v = [random.choice(firstname)]
        w = [random.choice(lastname) for i in range(2)]
        c = v + w
        return c


    def sex(self):  # 随机选择性别
        s = ['男', '女']
        x = str(random.choice(s))
        return x


    def education(self):  #随机选择文化程度
        s = ['初中', '高中', '本科', '博士', '硕士']
        x = str(random.choice(s))
        return x


    def department(self):  #随机选择部门
        s = ['销售部', '财务部']
        x = str(random.choice(s))
        return x

    def nation(self):  #随机选择民族
        d = ["汉族","蒙古族","回族","藏族","维吾尔族","苗族","彝族","壮族","布依族","朝鲜族","满族","侗族","瑶族","白族","土家族","哈尼族","哈萨克族","傣族","黎族","僳僳族","佤族",'畲族',"高山族","拉祜族","水族","东乡族","纳西族","景颇族","柯尔克孜族","土族","达斡尔族","仫佬族","羌族","布朗族","撒拉族","毛南族","仡佬族","锡伯族","阿昌族","普米族","塔吉克族","怒族","乌孜别克族","俄罗斯族","鄂温克族","德昂族","保安族","裕固族","京族","塔塔尔族","独龙族","鄂伦春族","赫哲族","门巴族","珞巴族","基诺族"]
        s = str(random.choice(d))
        return s

    def marry(self):  # 随机选择婚姻状况
        d = ['已婚', '未婚', '离异']
        s = str(random.choice(d))
        return s

    def role(self):  # 随机选择角色
        d = ['管理员','员工','老板']
        s = str(random.choice(d))
        return s

    def address(self):
        dress_1 = [str(random.choice(
            ["河北省", "山西省", "辽宁省", "吉林省", "黑龙江省", "江苏省", "浙江省", "安徽省", "福建省", "江西省", "山东省", "河南省", "湖北省", "湖南省", "广东省",
             "海南省", "四川省", "贵州省", "云南省", "陕西省", "甘肃省", "青海省", "台湾省", "内蒙古自治区", "广西壮族自治区", "西藏自治区", "宁夏回族自治区",
             "新疆维吾尔自治区",
             "北京市", "天津市", "上海市", "重庆市", "香港特别行政区", "澳门特别行政区"]))]
        dress_2 = [random.choice(
            ["北京", "上海", "广州", "深圳", "成都", "杭州", "佛山", "苏州", "西安", "天津", "上海", "北京", "深圳", "天津", "苏州", "重庆", "杭州", "武汉",
             "广州", "宁波", "广州", "北京", "上海", "南京", "杭州", "武汉", "深圳", "长沙", "苏州", "沈阳", "北京", "上海", "深圳", "广州", "天津", "杭州",
             "苏州", "南京", "重庆", "成都", "天津", "重庆", "武汉", "长沙", "青岛", "合肥", "郑州", "东营", "无锡", "南京"])]
        dress_3 = [random.choice(
            ["万州区", "涪陵区", "渝中区", "大渡口区", "江北区", "沙坪坝区", "九龙坡区", "南岸区", "北碚区", "万盛区", "双桥区", "渝北区", "巴南区", "黔江区", "长寿区",
             "江津区", "合川区", "永川区", "南川区綦江县", "潼南县", "铜梁县", "大足县", "荣昌县", "璧山县", "梁平县", "城口县", "丰都县", "垫江县", "武隆县", "忠县",
             "开县", "云阳县", "奉节县", "巫山县", "巫溪县", "石柱土家族自治县", "秀山土家族苗族自治县", "酉阳土家族苗族自治县", "彭水苗族土家族自治县"])]
        dress = ''.join(dress_1) + "".join(dress_2) + "".join(dress_3)
        return dress

    def email(self):
        e = ['@qq.com','@163.com', "@gmail.com","@yahoo.com","@msn.com","@hotmail.com","@aol.com","@ask.com","@live.com","@0355.net"]
        r = str(random.choice(e))
        a = [str(random.randint(1, 9))]
        v = [str(random.randint(0, 9)) for i in range(9)]
        w = ''.join(a)+''.join(v)+''.join(r)
        return w

    def habit(self):
        s = ['打篮球', '踢足球', '下象棋', '练跆拳道', '踢毽子', '打羽毛球']
        a = random.choice(s)
        return a





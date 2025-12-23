import streamlit as st
import random

# 设置页面
st.set_page_config(
    page_title="智能文案生成器",
    page_icon="💎",
    layout="wide"
)

st.title("智能文案生成器")

# ---------- 智能关键词库 ----------
KEYWORD_SYSTEM = {
    "火锅": {
        "recommend_keywords": ["麻辣", "鲜香", "毛肚", "鸭肠", "服务", "环境", "热闹", "过瘾", "牛油", "酥肉"],
        "dishes": ["鲜毛肚", "嫩牛肉", "手工虾滑", "黄喉", "鸭血", "脑花", "酥肉", "红糖糍粑"],
        "tastes": ["麻辣鲜香", "醇厚浓郁", "回味无穷", "香辣过瘾", "辣而不燥"],
        "environments": ["热闹温馨", "装修精致", "氛围浓厚", "干净整洁", "有特色"],
        "services": ["热情周到", "响应及时", "专业细致", "贴心服务", "态度友好"],
        "short_slogans": ["麻辣鲜香，回味无穷", "火锅界的扛把子", "一锅红油，万千滋味", "舌尖上的麻辣狂欢",
                          "冬日里的暖心选择"],
        "scenes": ["热闹的店面", "温馨的包厢", "明亮的吧台", "窗边位置", "包间雅座"],
        "actions": ["品尝美味", "享受服务", "与朋友畅聊", "拍照打卡", "享受美食"],
        "insights": ["美食的乐趣", "社交的温暖", "味蕾的享受", "生活的仪式感", "朋友的陪伴"]
    },
    "烧烤": {
        "recommend_keywords": ["炭火", "香气", "烤串", "啤酒", "夜宵", "聚会", "氛围", "调料", "新鲜", "烟火"],
        "dishes": ["羊肉串", "烤茄子", "烤韭菜", "烤馒头", "烤玉米", "烤鸡翅", "烤生蚝"],
        "tastes": ["孜然香气", "炭火味足", "外焦里嫩", "香辣可口", "咸淡适中"],
        "environments": ["烟火气息", "热闹非凡", "简约大方", "干净卫生", "有氛围"],
        "services": ["快速高效", "热情好客", "主动推荐", "及时上菜", "服务到位"],
        "short_slogans": ["炭火香气，美味在线", "夜宵首选，烧烤狂欢", "一串入魂，满口留香", "烧烤配啤酒，快乐常有",
                          "烟火气息，人间美味"],
        "scenes": ["烟火缭绕的烤架", "热闹的夜市", "户外座位", "深夜食堂", "朋友聚会角落"],
        "actions": ["享受宵夜", "畅饮啤酒", "朋友聚会", "品尝美食", "放松心情"],
        "insights": ["深夜的温暖", "友情的滋味", "生活的烟火气", "简单的快乐", "美食的治愈"]
    },
    "暗恋": {
        "recommend_keywords": ["青涩", "心动", "偷偷", "日记", "青春", "美好", "遗憾", "成长", "纯真", "脸红"],
        "emotions": ["小鹿乱撞", "忐忑不安", "甜蜜期待", "患得患失", "心跳加速"],
        "scenes": ["教室窗边", "操场跑道", "图书馆角落", "放学路上", "食堂排队"],
        "actions": ["偷看背影", "写日记", "制造偶遇", "听ta喜欢的歌", "保存聊天记录"],
        "insights": ["青涩的美好", "成长的代价", "纯真的感情", "青春的印记", "时间的礼物"],
        "short_slogans": ["青春里最美好的秘密", "藏在心底的喜欢", "偷偷喜欢，慢慢长大", "暗恋是一场独角戏",
                          "那些没说出口的喜欢"],
        "stages": ["初次心动", "默默关注", "期待相遇", "反复思量", "珍藏心底"],
        "methods": ["写日记", "听歌思念", "偷偷关注", "制造偶遇", "默默祝福"],
        "gains": ["成长经历", "美好回忆", "纯真情感", "青春印记", "自我认识"]
    },
    "失恋": {
        "recommend_keywords": ["痛苦", "眼泪", "时间", "疗愈", "成长", "放下", "释怀", "坚强", "重生", "独立"],
        "emotions": ["心如刀割", "泪流满面", "失魂落魄", "痛苦挣扎", "慢慢释怀"],
        "stages": ["初期痛苦", "反复挣扎", "逐渐接受", "开始成长", "真正放下"],
        "methods": ["时间疗伤", "朋友陪伴", "自我提升", "转移注意", "接纳现实"],
        "gains": ["更加坚强", "更懂自己", "珍惜当下", "成长成熟", "重新出发"],
        "short_slogans": ["告别过去，迎接新生", "失恋是成长的开始", "放下是为了更好的开始", "时间是治愈的良药",
                          "失恋后，我长大了"],
        "scenes": ["一个人的房间", "熟悉的街道", "曾经约会的餐厅", "雨中漫步", "深夜思考"],
        "actions": ["回忆过往", "整理心情", "重新出发", "自我反思", "寻找新方向"],
        "insights": ["成长的痛", "自我发现", "重新开始", "时间的治愈", "生命的韧性"]
    },
    "旅行": {
        "recommend_keywords": ["风景", "探索", "自由", "文化", "体验", "记忆", "冒险", "放松", "发现", "摄影"],
        "attractions": ["古镇小巷", "山川湖海", "历史遗迹", "现代都市", "自然风光"],
        "feelings": ["心灵放松", "视野开阔", "文化震撼", "自由自在", "难忘体验"],
        "experiences": ["当地美食", "特色文化", "风土人情", "独特风景", "深度探索"],
        "harvests": ["美好回忆", "成长见识", "心灵洗涤", "放松心情", "开阔眼界"],
        "short_slogans": ["在路上，遇见更好的自己", "世界那么大，我想去看看", "旅行让心灵自由飞翔", "每一次出发都是新生",
                          "风景在远方，梦想在路上"],
        "scenes": ["壮丽的风景", "异国的街道", "宁静的海边", "热闹的市集", "山顶的日出"],
        "actions": ["探索未知", "拍照记录", "品尝美食", "体验文化", "享受自由"],
        "insights": ["世界的广阔", "生命的多彩", "心灵的自由", "人生的意义", "成长的眼界"],
        "emotions": ["惊喜发现", "心灵震撼", "自由快乐", "感慨万千", "感恩遇见"],
        "methods": ["规划行程", "探索发现", "记录感受", "融入当地", "分享经历"],
        "gains": ["美好回忆", "开阔眼界", "心灵成长", "人生感悟", "新的视角"]
    },
    "读书": {
        "recommend_keywords": ["思考", "智慧", "安静", "沉浸", "启发", "知识", "心灵", "成长", "世界", "感悟"],
        "types": ["文学经典", "历史传记", "哲学思考", "心理学", "自我成长"],
        "feelings": ["心灵共鸣", "思想启迪", "知识增长", "内心平静", "视野开阔"],
        "harvests": ["思维升级", "认知提升", "情感丰富", "智慧增长", "内心强大"],
        "methods": ["深度阅读", "思考笔记", "实践应用", "分享讨论", "反复品味"],
        "short_slogans": ["书中自有黄金屋", "阅读让灵魂更丰富", "一本好书，一个世界", "在书海中寻找智慧",
                          "读书是最好的投资"],
        "scenes": ["安静的书房", "阳光的窗边", "咖啡馆角落", "图书馆座位", "深夜的台灯下"],
        "actions": ["沉浸阅读", "思考笔记", "分享感悟", "实践应用", "反复品味"],
        "insights": ["知识的价值", "思想的深度", "心灵的成长", "人生的智慧", "世界的理解"],
        "emotions": ["内心平静", "思想启迪", "心灵震撼", "情感共鸣", "知识满足"],
        "stages": ["开始阅读", "深入理解", "思考感悟", "实践应用", "分享交流"]
    }
}


# ---------- 智能内容生成 ----------
class SmartGenerator:
    def __init__(self):
        pass

    def get_recommended_keywords(self, topic):
        """智能推荐关键词"""
        topic_lower = topic.lower()
        if any(word in topic_lower for word in ["火锅", "麻辣", "涮锅"]):
            return KEYWORD_SYSTEM["火锅"]["recommend_keywords"]
        elif any(word in topic_lower for word in ["烧烤", "烤串", "烤肉"]):
            return KEYWORD_SYSTEM["烧烤"]["recommend_keywords"]
        elif any(word in topic_lower for word in ["暗恋", "初恋", "喜欢"]):
            return KEYWORD_SYSTEM["暗恋"]["recommend_keywords"]
        elif any(word in topic_lower for word in ["失恋", "分手", "结束"]):
            return KEYWORD_SYSTEM["失恋"]["recommend_keywords"]
        elif any(word in topic_lower for word in ["旅行", "旅游", "游记"]):
            return KEYWORD_SYSTEM["旅行"]["recommend_keywords"]
        elif any(word in topic_lower for word in ["读书", "阅读", "书籍"]):
            return KEYWORD_SYSTEM["读书"]["recommend_keywords"]
        else:
            return ["体验", "感受", "成长", "思考", "收获", "记忆", "价值", "意义"]

    def get_topic_data(self, topic):
        """获取主题相关数据"""
        topic_lower = topic.lower()
        if any(word in topic_lower for word in ["火锅", "麻辣", "涮锅"]):
            return KEYWORD_SYSTEM["火锅"]
        elif any(word in topic_lower for word in ["烧烤", "烤串", "烤肉"]):
            return KEYWORD_SYSTEM["烧烤"]
        elif any(word in topic_lower for word in ["暗恋", "初恋", "喜欢"]):
            return KEYWORD_SYSTEM["暗恋"]
        elif any(word in topic_lower for word in ["失恋", "分手", "结束"]):
            return KEYWORD_SYSTEM["失恋"]
        elif any(word in topic_lower for word in ["旅行", "旅游", "游记"]):
            return KEYWORD_SYSTEM["旅行"]
        elif any(word in topic_lower for word in ["读书", "阅读", "书籍"]):
            return KEYWORD_SYSTEM["读书"]
        else:
            default_data = KEYWORD_SYSTEM["暗恋"].copy()
            required_keys = ["scenes", "actions", "insights", "emotions", "stages", "methods", "gains", "short_slogans"]
            for key in required_keys:
                if key not in default_data:
                    default_data[key] = [f"默认{key}"]
            return default_data

    def generate_content(self, topic, style, length="标准长度", user_keywords=""):
        """智能生成内容"""
        try:
            topic_data = self.get_topic_data(topic)
            is_food = "dishes" in topic_data

            if user_keywords:
                user_kw_list = [k.strip() for k in user_keywords.split(',') if k.strip()]
                recommended = topic_data["recommend_keywords"][:3]
                all_keywords = user_kw_list + recommended
            else:
                all_keywords = topic_data["recommend_keywords"][:5]

            if length == "超短文案":
                return self._generate_ultra_short(topic, topic_data, all_keywords, is_food)

            if style == "感性叙事":
                content = self._generate_emotional(topic, topic_data, all_keywords, is_food)
            elif style == "理性分析":
                content = self._generate_rational(topic, topic_data, all_keywords, is_food)
            elif style == "专业测评":
                content = self._generate_professional(topic, topic_data, all_keywords, is_food)
            elif style == "轻松活泼":
                content = self._generate_casual(topic, topic_data, all_keywords, is_food)
            elif style == "深度思考":
                content = self._generate_philosophical(topic, topic_data, all_keywords, is_food)
            else:
                content = self._generate_emotional(topic, topic_data, all_keywords, is_food)

            return self._adjust_content_length(content, length)
        except Exception as e:
            st.error(f"生成内容时出错：{str(e)}")
            return f"关于「{topic}」的{style}分享。"

    def _generate_ultra_short(self, topic, topic_data, keywords, is_food):
        """生成超短文案"""
        try:
            short_slogans = topic_data.get("short_slogans", [f"{topic}，值得一试"])
            return random.choice(short_slogans)
        except:
            return f"{topic}，精彩！"

    def _generate_emotional(self, topic, topic_data, keywords, is_food):
        """生成感性叙事"""
        if is_food:
            dish = random.choice(topic_data.get("dishes", ["美食"]))
            taste = random.choice(topic_data.get("tastes", ["美味"]))
            env = random.choice(topic_data.get("environments", ["舒适环境"]))
            service = random.choice(topic_data.get("services", ["周到服务"]))

            return f"""关于「{topic}」的记忆，总是伴随着{taste}的诱惑。

走进店里，{env}的氛围让人倍感舒适。{dish}在锅里翻滚，让人食欲大开。

最难忘的是朋友围坐的欢声笑语，{service}的服务让用餐过程更加舒心。"""
        else:
            emotion = random.choice(topic_data.get("emotions", ["感动"]))
            scene = random.choice(topic_data.get("scenes", ["某个地方"]))
            insight = random.choice(topic_data.get("insights", ["感悟"]))

            return f"""关于「{topic}」，那些藏在心底的记忆依然温暖。

还记得{scene}的那个午后，{emotion}的感觉悄然生长。

那段经历教会了我{insight}，现在回想起来依然会微笑。"""

    def _generate_rational(self, topic, topic_data, keywords, is_food):
        """生成理性分析"""
        if is_food:
            dish = random.choice(topic_data.get("dishes", ["特色菜"]))
            taste = random.choice(topic_data.get("tastes", ["美味"]))
            env = random.choice(topic_data.get("environments", ["舒适环境"]))
            service = random.choice(topic_data.get("services", ["良好服务"]))

            return f"""「{topic}」分析

环境：{env}
菜品：{dish}
口味：{taste}
服务：{service}

人均：80-150元
综合评分：8.5/10"""
        else:
            emotion = random.choice(topic_data.get("emotions", ["情感"]))
            stage = random.choice(topic_data.get("stages", ["过程"]))
            gain = random.choice(topic_data.get("gains", ["成长"]))

            return f"""「{topic}」分析

情感类型：{emotion}
发展阶段：{stage}
长期收获：{gain}

建议：理性对待，视为成长的一部分。"""

    def _generate_professional(self, topic, topic_data, keywords, is_food):
        """生成专业测评"""
        if is_food:
            dish1 = random.choice(topic_data.get("dishes", ["招牌菜"]))
            taste = random.choice(topic_data.get("tastes", ["美味"]))
            service = random.choice(topic_data.get("services", ["专业服务"]))

            return f"""「{topic}」测评

锅底：9/10 ({taste})
招牌菜：{dish1} 9.5/10
环境：8/10
服务：8/10 ({service})

综合得分：8.6/10
推荐指数：⭐⭐⭐⭐"""
        else:
            emotion = random.choice(topic_data.get("emotions", ["情感"]))
            insight = random.choice(topic_data.get("insights", ["成长"]))

            return f"""「{topic}」心理测评

情感深度：8/10 ({emotion})
成长价值：9/10 (促进{insight})

推荐指数：⭐⭐⭐⭐"""

    def _generate_casual(self, topic, topic_data, keywords, is_food):
        """生成轻松活泼"""
        if is_food:
            dish = random.choice(topic_data.get("dishes", ["美食"]))
            taste = random.choice(topic_data.get("tastes", ["美味"]))

            return f"""「{topic}」真的绝了！

{taste}的味道浓郁，{dish}好吃到爆炸！

人均100+吃到扶墙出，性价比超高！

按头安利给所有吃货朋友！"""
        else:
            emotion = random.choice(topic_data.get("emotions", ["兴奋"]))
            action = random.choice(topic_data.get("actions", ["经历"]))

            return f"""关于「{topic}」有太多话要说！

那种{emotion}的感觉真的上头！

{action}的时候心跳加速到不行！

现在想想还是会忍不住微笑呢～"""

    def _generate_philosophical(self, topic, topic_data, keywords, is_food):
        """生成深度思考"""
        if is_food:
            taste = random.choice(topic_data.get("tastes", ["美味"]))

            return f"""「{topic}」：饮食文化的思考

{topic}不仅是一种味觉享受，更是一种情感载体。

在{taste}的刺激中，人们卸下伪装，回归真实。

围坐一桌的亲密，分享食物的温暖。

一顿美食，一次情感的交流，一场生活的仪式。"""
        else:
            emotion = random.choice(topic_data.get("emotions", ["情感"]))
            insight = random.choice(topic_data.get("insights", ["价值"]))

            return f"""「{topic}」：关于情感的思考

{topic}不仅是一种情感体验，更是个体与世界关系的镜像。

在{emotion}的情感投射中，我们看到的究竟是对方，还是自我理想的倒影？

在不确定的世界中，我们通过情感投入来确认自身的{insight}和价值。"""

    def _adjust_content_length(self, content, length):
        """调整内容长度"""
        words = len(content)

        if length == "超短文案":
            if words <= 10:
                return content
            else:
                sentences = content.split('。')
                if sentences:
                    return sentences[0][:10]
                return content[:10]
        elif length == "短篇精简":
            if 10 <= words <= 50:
                return content
            elif words > 50:
                return content[:50]
            else:
                return content + "。" * (10 - words)
        elif length == "标准长度":
            if 50 <= words <= 200:
                return content
            elif words > 200:
                return content[:200]
            else:
                return content
        else:  # 详细长文
            if words >= 200:
                return content
            else:
                return content + " " * (200 - words)


# ---------- 初始化 ----------
generator = SmartGenerator()

# ---------- 主界面 ----------
st.subheader("创作主题")
topic = st.text_input(
    "请输入您的创作主题",
    value="重庆火锅探店",
    placeholder="例如：学生时代的暗恋、烧烤店体验、旅行回忆"
)

if topic:
    recommended_keywords = generator.get_recommended_keywords(topic)
    recommended_str = "、".join(recommended_keywords[:8])

    st.subheader("关键词设置")

    col1, col2 = st.columns([3, 1])

    with col1:
        user_keywords = st.text_input(
            "输入关键词（用逗号分隔）",
            placeholder="例如：麻辣、毛肚、服务、环境"
        )

    with col2:
        if st.button("使用推荐"):
            st.session_state.recommended_keywords = ",".join(recommended_keywords[:5])
            st.rerun()

    if "recommended_keywords" in st.session_state:
        user_keywords = st.session_state.recommended_keywords
        st.success(f"已使用推荐关键词：{st.session_state.recommended_keywords}")

    st.info(f"智能推荐关键词：{recommended_str}")

st.subheader("写作风格")
style = st.radio(
    "选择写作风格",
    ["感性叙事", "理性分析", "专业测评", "轻松活泼", "深度思考"],
    horizontal=True
)

st.subheader("内容长度")
length = st.radio(
    "选择内容长度",
    ["超短文案", "短篇精简", "标准长度", "详细长文"],
    horizontal=True,
    index=1
)

if st.button("生成智能文案", type="primary", use_container_width=True):
    if not topic:
        st.warning("请输入创作主题")
    else:
        content = generator.generate_content(topic, style, length, user_keywords)
        word_count = len(content)

        title_styles = {
            "感性叙事": f"{topic}：藏在时光里的温暖记忆",
            "理性分析": f"{topic}分析报告",
            "专业测评": f"{topic}测评报告",
            "轻松活泼": f"绝了！{topic}真的太上头了！",
            "深度思考": f"{topic}：关于文化与情感的思考"
        }
        title = title_styles.get(style, f"{topic}体验分享")

        st.session_state.current_result = {
            "title": title,
            "content": content,
            "word_count": word_count,
            "style": style,
            "length": length
        }

if "current_result" in st.session_state:
    result = st.session_state.current_result

    st.markdown("---")

    if result['length'] == "超短文案":
        st.markdown(f"## 超短文案")
        st.markdown(f"# {result['content']}")
    else:
        st.markdown(f"# {result['title']}")

    st.metric("当前字数", f"{result['word_count']}字")

    st.markdown("---")

    if result['length'] != "超短文案":
        st.markdown(result['content'])

    st.markdown("---")
    st.subheader("复制文案")

    full_text = f"{result['title']}\n\n{result['content']}"
    st.code(full_text, language="text")

    col_copy1, col_copy2 = st.columns(2)
    with col_copy1:
        st.download_button(
            label="下载文案",
            data=full_text,
            file_name=f"{result['style']}_{topic}.txt",
            mime="text/plain",
            use_container_width=True
        )
    with col_copy2:
        if st.button("重新生成", use_container_width=True):
            del st.session_state.current_result
            st.rerun()

# 侧边栏
with st.sidebar:
    st.markdown("## 使用说明")
    st.markdown("""
    输入主题后，系统会推荐相关关键词。

    选择喜欢的写作风格和内容长度。

    点击生成按钮即可获得智能文案。

    支持美食、情感、旅行、读书等主题。
    """)
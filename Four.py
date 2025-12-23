import streamlit as st
import random
import json

# 设置页面
st.set_page_config(
    page_title="智能文案生成器",
    page_icon="✨",
    layout="wide"
)

st.title("✨ 智能文案生成器")

# ---------- 智能关键词库 ----------
KEYWORD_SYSTEM = {
    "火锅": {
        "recommend_keywords": ["麻辣", "鲜香", "毛肚", "鸭肠", "服务", "环境", "热闹", "过瘾", "牛油", "酥肉"],
        "dishes": ["鲜毛肚", "嫩牛肉", "手工虾滑", "黄喉", "鸭血", "脑花", "酥肉", "红糖糍粑"],
        "tastes": ["麻辣鲜香", "醇厚浓郁", "回味无穷", "香辣过瘾", "辣而不燥"],
        "environments": ["热闹温馨", "装修精致", "氛围浓厚", "干净整洁", "有特色"],
        "services": ["热情周到", "响应及时", "专业细致", "贴心服务", "态度友好"],
        "short_slogans": ["麻辣鲜香，回味无穷", "火锅界的扛把子", "一锅红油，万千滋味", "舌尖上的麻辣狂欢",
                          "冬日里的暖心选择"]
    },
    "烧烤": {
        "recommend_keywords": ["炭火", "香气", "烤串", "啤酒", "夜宵", "聚会", "氛围", "调料", "新鲜", "烟火"],
        "dishes": ["羊肉串", "烤茄子", "烤韭菜", "烤馒头", "烤玉米", "烤鸡翅", "烤生蚝"],
        "tastes": ["孜然香气", "炭火味足", "外焦里嫩", "香辣可口", "咸淡适中"],
        "environments": ["烟火气息", "热闹非凡", "简约大方", "干净卫生", "有氛围"],
        "services": ["快速高效", "热情好客", "主动推荐", "及时上菜", "服务到位"],
        "short_slogans": ["炭火香气，美味在线", "夜宵首选，烧烤狂欢", "一串入魂，满口留香", "烧烤配啤酒，快乐常有",
                          "烟火气息，人间美味"]
    },
    "暗恋": {
        "recommend_keywords": ["青涩", "心动", "偷偷", "日记", "青春", "美好", "遗憾", "成长", "纯真", "脸红"],
        "emotions": ["小鹿乱撞", "忐忑不安", "甜蜜期待", "患得患失", "心跳加速"],
        "scenes": ["教室窗边", "操场跑道", "图书馆角落", "放学路上", "食堂排队"],
        "actions": ["偷看背影", "写日记", "制造偶遇", "听ta喜欢的歌", "保存聊天记录"],
        "insights": ["青涩的美好", "成长的代价", "纯真的感情", "青春的印记", "时间的礼物"],
        "short_slogans": ["青春里最美好的秘密", "藏在心底的喜欢", "偷偷喜欢，慢慢长大", "暗恋是一场独角戏",
                          "那些没说出口的喜欢"]
    },
    "失恋": {
        "recommend_keywords": ["痛苦", "眼泪", "时间", "疗愈", "成长", "放下", "释怀", "坚强", "重生", "独立"],
        "emotions": ["心如刀割", "泪流满面", "失魂落魄", "痛苦挣扎", "慢慢释怀"],
        "stages": ["初期痛苦", "反复挣扎", "逐渐接受", "开始成长", "真正放下"],
        "methods": ["时间疗伤", "朋友陪伴", "自我提升", "转移注意", "接纳现实"],
        "gains": ["更加坚强", "更懂自己", "珍惜当下", "成长成熟", "重新出发"],
        "short_slogans": ["告别过去，迎接新生", "失恋是成长的开始", "放下是为了更好的开始", "时间是治愈的良药",
                          "失恋后，我长大了"]
    },
    "旅行": {
        "recommend_keywords": ["风景", "探索", "自由", "文化", "体验", "记忆", "冒险", "放松", "发现", "摄影"],
        "attractions": ["古镇小巷", "山川湖海", "历史遗迹", "现代都市", "自然风光"],
        "feelings": ["心灵放松", "视野开阔", "文化震撼", "自由自在", "难忘体验"],
        "experiences": ["当地美食", "特色文化", "风土人情", "独特风景", "深度探索"],
        "harvests": ["美好回忆", "成长见识", "心灵洗涤", "放松心情", "开阔眼界"],
        "short_slogans": ["在路上，遇见更好的自己", "世界那么大，我想去看看", "旅行让心灵自由飞翔", "每一次出发都是新生",
                          "风景在远方，梦想在路上"]
    },
    "读书": {
        "recommend_keywords": ["思考", "智慧", "安静", "沉浸", "启发", "知识", "心灵", "成长", "世界", "感悟"],
        "types": ["文学经典", "历史传记", "哲学思考", "心理学", "自我成长"],
        "feelings": ["心灵共鸣", "思想启迪", "知识增长", "内心平静", "视野开阔"],
        "harvests": ["思维升级", "认知提升", "情感丰富", "智慧增长", "内心强大"],
        "methods": ["深度阅读", "思考笔记", "实践应用", "分享讨论", "反复品味"],
        "short_slogans": ["书中自有黄金屋", "阅读让灵魂更丰富", "一本好书，一个世界", "在书海中寻找智慧",
                          "读书是最好的投资"]
    }
}


# ---------- 词库管理器 ----------
class KeywordManager:
    def __init__(self):
        # 深拷贝默认词库
        self.keyword_system = {k: v.copy() for k, v in KEYWORD_SYSTEM.items()}

    def import_json(self, json_str):
        """导入JSON格式词库"""
        try:
            custom_data = json.loads(json_str)
            imported_count = 0

            for topic, data in custom_data.items():
                if topic in self.keyword_system:
                    # 合并到现有主题
                    for key, value in data.items():
                        if key in self.keyword_system[topic]:
                            # 如果是列表就合并
                            if isinstance(value, list):
                                self.keyword_system[topic][key] = list(set(self.keyword_system[topic][key] + value))
                            else:
                                self.keyword_system[topic][key] = value
                        else:
                            self.keyword_system[topic][key] = value
                else:
                    # 新增主题
                    self.keyword_system[topic] = data

                imported_count += 1

            return True, f"✅ 成功导入 {imported_count} 个主题！"
        except json.JSONDecodeError:
            return False, "❌ JSON格式错误！请检查格式。"
        except Exception as e:
            return False, f"❌ 导入失败：{str(e)}"

    def get_recommended_keywords(self, topic):
        """智能推荐关键词（使用当前词库）"""
        topic_lower = topic.lower()

        # 先精确匹配
        for key in self.keyword_system.keys():
            if key in topic_lower:
                return self.keyword_system[key].get("recommend_keywords", ["体验", "感受"])

        # 智能匹配
        if any(word in topic_lower for word in ["火锅", "麻辣", "涮锅"]):
            return self.keyword_system["火锅"]["recommend_keywords"]
        elif any(word in topic_lower for word in ["烧烤", "烤串", "烤肉"]):
            return self.keyword_system["烧烤"]["recommend_keywords"]
        elif any(word in topic_lower for word in ["暗恋", "初恋", "喜欢"]):
            return self.keyword_system["暗恋"]["recommend_keywords"]
        elif any(word in topic_lower for word in ["失恋", "分手", "结束"]):
            return self.keyword_system["失恋"]["recommend_keywords"]
        elif any(word in topic_lower for word in ["旅行", "旅游", "游记"]):
            return self.keyword_system["旅行"]["recommend_keywords"]
        elif any(word in topic_lower for word in ["读书", "阅读", "书籍"]):
            return self.keyword_system["读书"]["recommend_keywords"]
        else:
            return ["体验", "感受", "成长", "思考", "收获"]

    def get_topic_data(self, topic):
        """获取主题数据"""
        topic_lower = topic.lower()

        for key in self.keyword_system.keys():
            if key in topic_lower:
                return self.keyword_system[key]

        if any(word in topic_lower for word in ["火锅", "麻辣", "涮锅"]):
            return self.keyword_system["火锅"]
        elif any(word in topic_lower for word in ["烧烤", "烤串", "烤肉"]):
            return self.keyword_system["烧烤"]
        elif any(word in topic_lower for word in ["暗恋", "初恋", "喜欢"]):
            return self.keyword_system["暗恋"]
        elif any(word in topic_lower for word in ["失恋", "分手", "结束"]):
            return self.keyword_system["失恋"]
        elif any(word in topic_lower for word in ["旅行", "旅游", "游记"]):
            return self.keyword_system["旅行"]
        elif any(word in topic_lower for word in ["读书", "阅读", "书籍"]):
            return self.keyword_system["读书"]
        else:
            return self.keyword_system["暗恋"]


# ---------- 智能内容生成 ----------
class SmartGenerator:
    def __init__(self, keyword_manager):
        self.km = keyword_manager

    def generate_content(self, topic, style, length="标准长度", user_keywords=""):
        """智能生成内容"""
        topic_data = self.km.get_topic_data(topic)
        is_food = "dishes" in topic_data

        # 处理关键词
        if user_keywords:
            user_kw_list = [k.strip() for k in user_keywords.split(',') if k.strip()]
            recommended = topic_data.get("recommend_keywords", ["体验", "感受"])[:3]
            all_keywords = user_kw_list + recommended
        else:
            all_keywords = topic_data.get("recommend_keywords", ["体验", "感受"])[:5]

        if length == "超短文案":
            short_slogans = topic_data.get("short_slogans", [f"{topic}，值得一试"])
            return random.choice(short_slogans)

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

        return content

    def _generate_emotional(self, topic, topic_data, keywords, is_food):
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
        if is_food:
            dish = random.choice(topic_data.get("dishes", ["特色菜"]))
            taste = random.choice(topic_data.get("tastes", ["美味"]))
            env = random.choice(topic_data.get("environments", ["舒适环境"]))
            service = random.choice(topic_data.get("services", ["良好服务"]))

            return f"""📊 「{topic}」分析

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

            return f"""📊 「{topic}」分析

情感类型：{emotion}
发展阶段：{stage}
长期收获：{gain}

建议：理性对待，视为成长的一部分。"""

    def _generate_professional(self, topic, topic_data, keywords, is_food):
        if is_food:
            dish1 = random.choice(topic_data.get("dishes", ["招牌菜"]))
            taste = random.choice(topic_data.get("tastes", ["美味"]))
            service = random.choice(topic_data.get("services", ["专业服务"]))

            return f"""⭐️ 「{topic}」测评

锅底：9/10 ({taste})
招牌菜：{dish1} 9.5/10
环境：8/10
服务：8/10 ({service})

综合得分：8.6/10
推荐指数：⭐⭐⭐⭐"""
        else:
            emotion = random.choice(topic_data.get("emotions", ["情感"]))
            insight = random.choice(topic_data.get("insights", ["成长"]))

            return f"""⭐️ 「{topic}」心理测评

情感深度：8/10 ({emotion})
成长价值：9/10 (促进{insight})

推荐指数：⭐⭐⭐⭐"""

    def _generate_casual(self, topic, topic_data, keywords, is_food):
        if is_food:
            dish = random.choice(topic_data.get("dishes", ["美食"]))
            taste = random.choice(topic_data.get("tastes", ["美味"]))

            return f"""😄 「{topic}」真的绝了！

{taste}的味道浓郁，{dish}好吃到爆炸！

人均100+吃到扶墙出，性价比超高！

按头安利给所有吃货朋友！"""
        else:
            emotion = random.choice(topic_data.get("emotions", ["兴奋"]))
            action = random.choice(topic_data.get("actions", ["经历"]))

            return f"""😄 关于「{topic}」有太多话要说！

那种{emotion}的感觉真的上头！

{action}的时候心跳加速到不行！

现在想想还是会忍不住微笑呢～"""

    def _generate_philosophical(self, topic, topic_data, keywords, is_food):
        if is_food:
            taste = random.choice(topic_data.get("tastes", ["美味"]))

            return f"""💭 「{topic}」：饮食文化的思考

{topic}不仅是一种味觉享受，更是一种情感载体。

在{taste}的刺激中，人们卸下伪装，回归真实。

围坐一桌的亲密，分享食物的温暖。

一顿美食，一次情感的交流，一场生活的仪式。"""
        else:
            emotion = random.choice(topic_data.get("emotions", ["情感"]))
            insight = random.choice(topic_data.get("insights", ["价值"]))

            return f"""💭 「{topic}」：关于情感的思考

{topic}不仅是一种情感体验，更是个体与世界关系的镜像。

在{emotion}的情感投射中，我们看到的究竟是对方，还是自我理想的倒影？

在不确定的世界中，我们通过情感投入来确认自身的{insight}和价值。"""


# ---------- 初始化 ----------
keyword_manager = KeywordManager()
generator = SmartGenerator(keyword_manager)

# ---------- 侧边栏：词库上传 ----------
with st.sidebar:
    st.markdown("## 📚 词库管理")

    # 方法1：文件上传
    st.subheader("📁 上传词库文件")
    uploaded_file = st.file_uploader(
        "选择JSON文件上传",
        type=['json'],
        help="上传JSON格式的自定义词库"
    )

    if uploaded_file is not None:
        try:
            json_str = uploaded_file.getvalue().decode("utf-8")
            success, message = keyword_manager.import_json(json_str)
            if success:
                st.success(message)
            else:
                st.error(message)
        except Exception as e:
            st.error(f"文件读取失败：{str(e)}")

    # 方法2：文本输入
    st.subheader("📝 或粘贴JSON内容")
    json_input = st.text_area(
        "直接粘贴JSON词库",
        height=150,
        placeholder='{"咖啡": {"recommend_keywords": ["浓郁", "香醇"]}}'
    )

    if st.button("导入词库", key="import_btn"):
        if json_input:
            success, message = keyword_manager.import_json(json_input)
            if success:
                st.success(message)
            else:
                st.error(message)
        else:
            st.warning("请输入JSON内容")

    st.markdown("---")
    st.markdown("## 📖 使用说明")
    st.markdown("""
    **🔑 智能关键词功能**
    1. 输入主题后自动推荐
    2. 点击"使用推荐"一键填充

    **📚 词库管理**
    1. 上传JSON文件 或 粘贴JSON
    2. 可扩展现有主题
    3. 可添加全新主题

    **🎨 写作风格**
    - 5种不同风格可选
    - 智能适配主题类型
    """)

    # JSON格式示例
    with st.expander("📋 JSON格式示例"):
        st.code("""{
  "咖啡店": {
    "recommend_keywords": ["拿铁", "手冲", "环境", "音乐"],
    "tastes": ["香醇浓郁", "口感顺滑"],
    "short_slogans": ["一杯咖啡的时光"]
  }
}""")

# ---------- 主界面 ----------
st.subheader("🎯 创作主题")
topic = st.text_input(
    "请输入您的创作主题",
    value="重庆火锅探店",
    placeholder="例如：学生时代的暗恋、烧烤店体验、旅行回忆",
    help="支持美食、情感、旅行、读书等主题"
)

# 智能关键词推荐
if topic:
    recommended_keywords = keyword_manager.get_recommended_keywords(topic)
    recommended_str = "、".join(recommended_keywords[:8])

    st.subheader("🔑 关键词设置")

    col1, col2 = st.columns([3, 1])

    with col1:
        user_keywords = st.text_input(
            "输入关键词（用逗号分隔）",
            placeholder="例如：麻辣、毛肚、服务、环境",
            help="可以输入自己的关键词，或使用下方推荐"
        )

    with col2:
        if st.button("使用推荐", key="use_recommend"):
            st.session_state.recommended_keywords = ",".join(recommended_keywords[:5])
            st.rerun()

    if "recommended_keywords" in st.session_state:
        user_keywords = st.session_state.recommended_keywords
        st.success(f"✅ 已使用推荐关键词：{st.session_state.recommended_keywords}")

    st.info(f"💡 智能推荐关键词：{recommended_str}")

else:
    user_keywords = st.text_input(
        "输入关键词（用逗号分隔）",
        placeholder="例如：青涩、美好、成长",
        help="请输入2-5个关键词"
    )

# 风格选择
st.subheader("🎨 写作风格")
style = st.radio(
    "选择写作风格",
    ["感性叙事", "理性分析", "专业测评", "轻松活泼", "深度思考"],
    horizontal=True
)

# 内容长度
st.subheader("📏 内容长度")
length = st.radio(
    "选择内容长度",
    ["超短文案", "短篇精简", "标准长度", "详细长文"],
    horizontal=True,
    index=1
)

# 生成按钮
if st.button("🚀 生成智能文案", type="primary", use_container_width=True):
    if not topic:
        st.warning("请输入创作主题")
    else:
        content = generator.generate_content(topic, style, length, user_keywords)
        word_count = len(content.replace(' ', '').replace('\n', ''))

        title_styles = {
            "感性叙事": f"❤️ {topic}：藏在时光里的温暖记忆",
            "理性分析": f"📊 {topic}分析报告",
            "专业测评": f"⭐️ {topic}测评报告",
            "轻松活泼": f"😄 绝了！{topic}真的太上头了！",
            "深度思考": f"💭 {topic}：关于文化与情感的思考"
        }
        title = title_styles.get(style, f"{topic}体验分享")

        st.session_state.current_result = {
            "title": title,
            "content": content,
            "word_count": word_count,
            "style": style,
            "length": length,
            "keywords": user_keywords if user_keywords else "使用智能推荐"
        }

# ---------- 显示结果 ----------
if "current_result" in st.session_state:
    result = st.session_state.current_result

    st.markdown("---")

    if result['length'] == "超短文案":
        st.markdown(f"## 🎯 超短文案")
        st.markdown(f"# {result['content']}")
    else:
        st.markdown(f"# {result['title']}")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("📝 字数", f"{result['word_count']}字")
    with col2:
        st.metric("🎨 风格", result['style'])
    with col3:
        if result['keywords']:
            kw_display = result['keywords'].split(',')[0]
            if len(result['keywords'].split(',')) > 1:
                kw_display += " 等"
            st.metric("🔑 关键词", kw_display)

    st.markdown("---")

    if result['length'] != "超短文案":
        st.markdown(result['content'])

    st.markdown("---")
    st.subheader("📋 复制文案")

    full_text = f"{result['title']}\n\n{result['content']}"
    st.code(full_text, language="text")

    col_copy1, col_copy2 = st.columns(2)
    with col_copy1:
        st.download_button(
            label="📥 下载文案",
            data=full_text,
            file_name=f"{result['style']}_{topic}.txt",
            mime="text/plain",
            use_container_width=True
        )
    with col_copy2:
        if st.button("🔄 重新生成", use_container_width=True):
            del st.session_state.current_result
            st.rerun()
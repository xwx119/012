import streamlit as st
import random

# 设置页面
st.set_page_config(
    page_title="智能文案生成器",
    page_icon="✨",
    layout="wide"
)

st.title("✨ 智能文案生成器")

# ---------- 智能关键词库 ----------
KEYWORD_SYSTEM = {
    # 美食探店类
    "火锅": {
        "recommend_keywords": ["麻辣", "鲜香", "毛肚", "鸭肠", "服务", "环境", "热闹", "过瘾", "牛油", "酥肉"],
        "dishes": ["鲜毛肚", "嫩牛肉", "手工虾滑", "黄喉", "鸭血", "脑花", "酥肉", "红糖糍粑"],
        "tastes": ["麻辣鲜香", "醇厚浓郁", "回味无穷", "香辣过瘾", "辣而不燥"],
        "environments": ["热闹温馨", "装修精致", "氛围浓厚", "干净整洁", "有特色"],
        "services": ["热情周到", "响应及时", "专业细致", "贴心服务", "态度友好"],
        "short_slogans": ["麻辣鲜香，回味无穷", "火锅界的扛把子", "一锅红油，万千滋味", "舌尖上的麻辣狂欢",
                          "冬日里的暖心选择"],
        "scenes": ["热闹的店面", "温馨的包厢", "明亮的吧台", "窗边位置", "包间雅座"],  # 添加scenes
        "actions": ["品尝美味", "享受服务", "与朋友畅聊", "拍照打卡", "享受美食"],  # 添加actions
        "insights": ["美食的乐趣", "社交的温暖", "味蕾的享受", "生活的仪式感", "朋友的陪伴"]  # 添加insights
    },
    "烧烤": {
        "recommend_keywords": ["炭火", "香气", "烤串", "啤酒", "夜宵", "聚会", "氛围", "调料", "新鲜", "烟火"],
        "dishes": ["羊肉串", "烤茄子", "烤韭菜", "烤馒头", "烤玉米", "烤鸡翅", "烤生蚝"],
        "tastes": ["孜然香气", "炭火味足", "外焦里嫩", "香辣可口", "咸淡适中"],
        "environments": ["烟火气息", "热闹非凡", "简约大方", "干净卫生", "有氛围"],
        "services": ["快速高效", "热情好客", "主动推荐", "及时上菜", "服务到位"],
        "short_slogans": ["炭火香气，美味在线", "夜宵首选，烧烤狂欢", "一串入魂，满口留香", "烧烤配啤酒，快乐常有",
                          "烟火气息，人间美味"],
        "scenes": ["烟火缭绕的烤架", "热闹的夜市", "户外座位", "深夜食堂", "朋友聚会角落"],  # 添加scenes
        "actions": ["享受宵夜", "畅饮啤酒", "朋友聚会", "品尝美食", "放松心情"],  # 添加actions
        "insights": ["深夜的温暖", "友情的滋味", "生活的烟火气", "简单的快乐", "美食的治愈"]  # 添加insights
    },

    # 情感心理类
    "暗恋": {
        "recommend_keywords": ["青涩", "心动", "偷偷", "日记", "青春", "美好", "遗憾", "成长", "纯真", "脸红"],
        "emotions": ["小鹿乱撞", "忐忑不安", "甜蜜期待", "患得患失", "心跳加速"],
        "scenes": ["教室窗边", "操场跑道", "图书馆角落", "放学路上", "食堂排队"],
        "actions": ["偷看背影", "写日记", "制造偶遇", "听ta喜欢的歌", "保存聊天记录"],
        "insights": ["青涩的美好", "成长的代价", "纯真的感情", "青春的印记", "时间的礼物"],
        "short_slogans": ["青春里最美好的秘密", "藏在心底的喜欢", "偷偷喜欢，慢慢长大", "暗恋是一场独角戏",
                          "那些没说出口的喜欢"],
        "stages": ["初次心动", "默默关注", "期待相遇", "反复思量", "珍藏心底"],  # 添加stages
        "methods": ["写日记", "听歌思念", "偷偷关注", "制造偶遇", "默默祝福"],  # 添加methods
        "gains": ["成长经历", "美好回忆", "纯真情感", "青春印记", "自我认识"]  # 添加gains
    },
    "失恋": {
        "recommend_keywords": ["痛苦", "眼泪", "时间", "疗愈", "成长", "放下", "释怀", "坚强", "重生", "独立"],
        "emotions": ["心如刀割", "泪流满面", "失魂落魄", "痛苦挣扎", "慢慢释怀"],
        "stages": ["初期痛苦", "反复挣扎", "逐渐接受", "开始成长", "真正放下"],
        "methods": ["时间疗伤", "朋友陪伴", "自我提升", "转移注意", "接纳现实"],
        "gains": ["更加坚强", "更懂自己", "珍惜当下", "成长成熟", "重新出发"],
        "short_slogans": ["告别过去，迎接新生", "失恋是成长的开始", "放下是为了更好的开始", "时间是治愈的良药",
                          "失恋后，我长大了"],
        "scenes": ["一个人的房间", "熟悉的街道", "曾经约会的餐厅", "雨中漫步", "深夜思考"],  # 添加scenes
        "actions": ["回忆过往", "整理心情", "重新出发", "自我反思", "寻找新方向"],  # 添加actions
        "insights": ["成长的痛", "自我发现", "重新开始", "时间的治愈", "生命的韧性"]  # 添加insights
    },

    # 其他类别
    "旅行": {
        "recommend_keywords": ["风景", "探索", "自由", "文化", "体验", "记忆", "冒险", "放松", "发现", "摄影"],
        "attractions": ["古镇小巷", "山川湖海", "历史遗迹", "现代都市", "自然风光"],
        "feelings": ["心灵放松", "视野开阔", "文化震撼", "自由自在", "难忘体验"],
        "experiences": ["当地美食", "特色文化", "风土人情", "独特风景", "深度探索"],
        "harvests": ["美好回忆", "成长见识", "心灵洗涤", "放松心情", "开阔眼界"],
        "short_slogans": ["在路上，遇见更好的自己", "世界那么大，我想去看看", "旅行让心灵自由飞翔", "每一次出发都是新生",
                          "风景在远方，梦想在路上"],
        "scenes": ["壮丽的风景", "异国的街道", "宁静的海边", "热闹的市集", "山顶的日出"],  # 添加scenes
        "actions": ["探索未知", "拍照记录", "品尝美食", "体验文化", "享受自由"],  # 添加actions
        "insights": ["世界的广阔", "生命的多彩", "心灵的自由", "人生的意义", "成长的眼界"],  # 添加insights
        "emotions": ["惊喜发现", "心灵震撼", "自由快乐", "感慨万千", "感恩遇见"],  # 添加emotions
        "methods": ["规划行程", "探索发现", "记录感受", "融入当地", "分享经历"],  # 添加methods
        "gains": ["美好回忆", "开阔眼界", "心灵成长", "人生感悟", "新的视角"]  # 添加gains
    },
    "读书": {
        "recommend_keywords": ["思考", "智慧", "安静", "沉浸", "启发", "知识", "心灵", "成长", "世界", "感悟"],
        "types": ["文学经典", "历史传记", "哲学思考", "心理学", "自我成长"],
        "feelings": ["心灵共鸣", "思想启迪", "知识增长", "内心平静", "视野开阔"],
        "harvests": ["思维升级", "认知提升", "情感丰富", "智慧增长", "内心强大"],
        "methods": ["深度阅读", "思考笔记", "实践应用", "分享讨论", "反复品味"],
        "short_slogans": ["书中自有黄金屋", "阅读让灵魂更丰富", "一本好书，一个世界", "在书海中寻找智慧",
                          "读书是最好的投资"],
        "scenes": ["安静的书房", "阳光的窗边", "咖啡馆角落", "图书馆座位", "深夜的台灯下"],  # 添加scenes
        "actions": ["沉浸阅读", "思考笔记", "分享感悟", "实践应用", "反复品味"],  # 添加actions
        "insights": ["知识的价值", "思想的深度", "心灵的成长", "人生的智慧", "世界的理解"],  # 添加insights
        "emotions": ["内心平静", "思想启迪", "心灵震撼", "情感共鸣", "知识满足"],  # 添加emotions
        "stages": ["开始阅读", "深入理解", "思考感悟", "实践应用", "分享交流"]  # 添加stages
    }
}


# ---------- 智能内容生成 ----------
class SmartGenerator:
    def __init__(self):
        pass

    def get_recommended_keywords(self, topic):
        """智能推荐关键词"""
        topic_lower = topic.lower()

        # 匹配主题类型
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
            # 默认返回情感类，确保所有键都存在
            default_data = KEYWORD_SYSTEM["暗恋"].copy()
            # 确保所有必要的键都存在
            required_keys = ["scenes", "actions", "insights", "emotions", "stages", "methods", "gains", "short_slogans"]
            for key in required_keys:
                if key not in default_data:
                    default_data[key] = [f"默认{key}"]
            return default_data

    def generate_content(self, topic, style, length="标准长度", user_keywords=""):
        """智能生成内容"""
        try:
            # 获取主题数据
            topic_data = self.get_topic_data(topic)

            # 判断主题类型
            is_food = "dishes" in topic_data  # 美食类有dishes键

            # 处理关键词
            if user_keywords:
                # 使用用户输入的关键词
                user_kw_list = [k.strip() for k in user_keywords.split(',') if k.strip()]
                # 合并推荐关键词
                recommended = topic_data["recommend_keywords"][:3]
                all_keywords = user_kw_list + recommended
            else:
                # 使用推荐关键词
                all_keywords = topic_data["recommend_keywords"][:5]

            # 如果是超短文案，直接返回
            if length == "超短文案":
                return self._generate_ultra_short(topic, topic_data, all_keywords, is_food)

            # 根据风格生成内容
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

            # 根据选择的长度调整内容
            return self._adjust_content_length(content, length)
        except KeyError as e:
            st.error(f"生成内容时出错：缺少键 {e}")
            return f"关于「{topic}」的{style}分享。这是一个美好的体验，让人印象深刻。"

    def _generate_ultra_short(self, topic, topic_data, keywords, is_food):
        """生成超短文案（10字以内）"""
        try:
            # 从关键词中提取
            keywords_for_short = keywords[:3] if keywords else ["体验", "感受"]

            # 获取主题的短句库
            if "short_slogans" in topic_data:
                short_slogans = topic_data["short_slogans"]
            else:
                # 如果没有预定义的短句，生成一些通用短句
                short_slogans = [
                    f"{topic}，极致体验",
                    f"关于{topic}的美好",
                    f"{topic}的魅力所在",
                    f"发现{topic}的美",
                    f"{topic}，值得一试"
                ]

            # 生成不同类型的超短文案
            short_templates = [
                # 简单描述型（3-5字）
                f"{random.choice(keywords_for_short)}·{topic}",
                f"{topic}：{random.choice(keywords_for_short)}",

                # 口号型（5-8字）
                random.choice(short_slogans),

                # 感叹型（4-7字）
                f"绝了！{topic}！",
                f"{topic}，太赞了！",
                f"爱上{topic}的感觉",

                # 对比型（6-10字）
                f"{topic}，不一样的体验",
                f"从{topic}开始的美好",
                f"{topic}：生活的小确幸",

                # 建议型（5-9字）
                f"推荐这个{topic}！",
                f"{topic}，值得拥有",
                f"来试试这个{topic}",

                # 情感型（4-8字）
                f"想念那个{topic}",
                f"{topic}，难忘的记忆",
                f"心中的{topic}情结"
            ]

            # 确保长度在10字以内
            ultra_short_options = []
            for option in short_templates:
                if len(option) <= 10:
                    ultra_short_options.append(option)

            # 如果没有合适的选项，生成一个简单的
            if not ultra_short_options:
                if is_food:
                    ultra_short_options = [f"{topic}，美味！", f"好吃！{topic}"]
                else:
                    ultra_short_options = [f"{topic}，感悟", f"关于{topic}"]

            return random.choice(ultra_short_options)
        except:
            return f"{topic}，精彩！"

    def _adjust_content_length(self, content, length):
        """根据选择的长度调整内容"""
        try:
            # 计算当前字数（中文字符）
            char_count = len(content.replace(' ', '').replace('\n', ''))

            # 根据选择的长度目标调整
            if length == "超短文案":
                # 目标：10字以内
                target_max = 10
                return self._shorten_to_ultra_short(content, target_max)
            elif length == "短篇精简":
                # 目标：10-50字
                target_min, target_max = 10, 50
            elif length == "标准长度":
                # 目标：50-200字
                target_min, target_max = 50, 200
            elif length == "详细长文":
                # 目标：200-300字
                target_min, target_max = 200, 300
            else:
                target_min, target_max = 50, 200  # 默认值

            # 根据当前字数与目标调整
            if char_count < target_min:
                # 内容过短，需要扩充
                return self._expand_content(content, target_min)
            elif char_count > target_max:
                # 内容过长，需要精简
                return self._shorten_content(content, target_max)
            else:
                # 长度合适，直接返回
                return content
        except:
            return content

    def _shorten_to_ultra_short(self, content, max_length):
        """将内容精简到10字以内"""
        try:
            # 先尝试提取最精华的部分
            sentences = content.replace('\n', ' ').split('。')

            # 找到最短的有意义的句子
            short_options = []
            for sentence in sentences:
                clean_sent = sentence.strip()
                if clean_sent and len(clean_sent) <= max_length:
                    short_options.append(clean_sent)

            if short_options:
                # 选择最短的
                return min(short_options, key=len)

            # 如果没有合适的句子，从内容中提取关键词
            words = content.replace('\n', ' ').replace('。', ' ').split()
            if len(words) >= 2:
                short_text = f"{words[0]}·{words[1]}"
                if len(short_text) <= max_length:
                    return short_text

            # 最后的手段：取前几个字
            return content[:max_length] if len(content) > max_length else content
        except:
            return content[:max_length] if len(content) > max_length else content

    def _expand_content(self, content, target_min):
        """扩充内容到目标字数"""
        try:
            sentences = content.split('\n\n')
            expanded_content = content

            # 如果段落太少，添加更多描述
            while len(expanded_content.replace(' ', '').replace('\n', '')) < target_min and len(sentences) < 5:
                # 判断内容类型
                is_food = any(word in expanded_content for word in ["火锅", "烧烤", "美食", "菜品", "味道"])

                if is_food:
                    additions = [
                        "每一口都是味蕾的惊喜，让人回味无穷。",
                        "这样的美食体验，值得与朋友分享。",
                        "无论是环境还是口味，都让人印象深刻。",
                        "这里的美食不仅满足味蕾，更温暖人心。",
                        "推荐给所有热爱美食的朋友们。"
                    ]
                else:
                    additions = [
                        "这样的经历，是生命中宝贵的财富。",
                        "每一次回忆，都让人心生温暖。",
                        "成长的过程，充满了这样的美好瞬间。",
                        "这些体验塑造了今天的我们。",
                        "感谢所有让我们成长的人和事。"
                    ]

                expanded_content += "\n\n" + random.choice(additions)

            return expanded_content
        except:
            return content

    def _shorten_content(self, content, target_max):
        """精简内容到目标字数"""
        try:
            # 按段落拆分
            paragraphs = [p.strip() for p in content.split('\n\n') if p.strip()]

            if not paragraphs:
                return content

            # 保留关键段落
            if len(paragraphs) > 3:
                # 保留开头、中间和结尾
                shortened = [paragraphs[0], paragraphs[len(paragraphs) // 2], paragraphs[-1]]
            else:
                shortened = paragraphs

            # 进一步精简每个段落
            result_paragraphs = []
            current_length = 0

            for para in shortened:
                if current_length >= target_max:
                    break

                # 精简段落内容
                if len(para) > 50:
                    # 取前50字
                    short_para = para[:50] + "..."
                else:
                    short_para = para

                result_paragraphs.append(short_para)
                current_length += len(short_para.replace(' ', '').replace('\n', ''))

            return '\n\n'.join(result_paragraphs)
        except:
            return content

    def _generate_emotional(self, topic, topic_data, keywords, is_food):
        """生成感性叙事"""
        try:
            if is_food:
                # 美食类感性内容
                dish = random.choice(topic_data.get("dishes", ["美食"]))
                taste = random.choice(topic_data.get("tastes", ["美味"]))
                env = random.choice(topic_data.get("environments", ["舒适环境"]))
                service = random.choice(topic_data.get("services", ["周到服务"]))
                kw1 = keywords[0] if len(keywords) > 0 else "美味"

                content = f"""关于「{topic}」的记忆，总是伴随着{taste}的诱惑。

走进店里，{env}的氛围让人倍感舒适。{dish}在锅里翻滚，让人食欲大开。

最难忘的是朋友围坐的欢声笑语，{service}的服务让用餐过程更加舒心。

美食的魅力，就在于它能让人在热气中找到温暖，在{kw1}中感受生活的热烈。"""
            else:
                # 情感类感性内容
                emotion = random.choice(topic_data.get("emotions", ["感动"]))
                scene = random.choice(topic_data.get("scenes", ["某个地方"]))
                action = random.choice(topic_data.get("actions", ["经历"]))
                insight = random.choice(topic_data.get("insights", ["感悟"]))

                content = f"""关于「{topic}」，那些藏在心底的记忆依然温暖。

还记得{scene}的那个午后，{emotion}的感觉悄然生长。那些{action}的日子。

最难忘的瞬间，至今想起依然会微笑。那段经历教会了我{insight}。

现在回想起来，{topic}虽不完美，却足够珍贵。"""
        except:
            content = f"""关于「{topic}」的美好回忆。

这是一次难忘的经历，让人心生温暖，收获成长。

每一次回想，都会让人微笑。这就是{topic}的魅力。"""

        return content

    def _generate_rational(self, topic, topic_data, keywords, is_food):
        """生成理性分析"""
        try:
            if is_food:
                # 美食类理性分析
                dish = random.choice(topic_data.get("dishes", ["特色菜"]))
                taste = random.choice(topic_data.get("tastes", ["美味"]))
                env = random.choice(topic_data.get("environments", ["舒适环境"]))
                service = random.choice(topic_data.get("services", ["良好服务"]))

                content = f"""📊 「{topic}」分析

环境：{env}
菜品：{dish}
口味：{taste}
服务：{service}

人均：80-150元
综合评分：8.5/10"""
            else:
                # 情感类理性分析
                emotion = random.choice(topic_data.get("emotions", ["情感"]))
                stage = random.choice(topic_data.get("stages", ["过程"]))
                gain = random.choice(topic_data.get("gains", ["成长"]))

                content = f"""📊 「{topic}」分析

情感类型：{emotion}
发展阶段：{stage}
长期收获：{gain}

建议：理性对待，视为成长的一部分。"""
        except:
            content = f"""📊 「{topic}」分析报告

这是一次有价值的体验，具有积极意义。

建议：客观看待，从中学习成长。"""

        return content

    def _generate_professional(self, topic, topic_data, keywords, is_food):
        """生成专业测评"""
        try:
            if is_food:
                # 美食类专业测评
                dish1 = random.choice(topic_data.get("dishes", ["招牌菜"]))
                taste = random.choice(topic_data.get("tastes", ["美味"]))
                service = random.choice(topic_data.get("services", ["专业服务"]))

                content = f"""⭐️ 「{topic}」测评

锅底：9/10 ({taste})
招牌菜：{dish1} 9.5/10
环境：8/10
服务：8/10 ({service})

综合得分：8.6/10
推荐指数：⭐⭐⭐⭐"""
            else:
                # 情感类专业测评
                emotion = random.choice(topic_data.get("emotions", ["情感"]))
                insight = random.choice(topic_data.get("insights", ["成长"]))

                content = f"""⭐️ 「{topic}」心理测评

情感深度：8/10 ({emotion})
成长价值：9/10 (促进{insight})

推荐指数：⭐⭐⭐⭐"""
        except:
            content = f"""⭐️ 「{topic}」专业测评

体验价值：8.5/10
成长意义：9/10

推荐指数：⭐⭐⭐"""

        return content

    def _generate_casual(self, topic, topic_data, keywords, is_food):
        """生成轻松活泼"""
        try:
            if is_food:
                # 美食类轻松内容
                dish = random.choice(topic_data.get("dishes", ["美食"]))
                taste = random.choice(topic_data.get("tastes", ["美味"]))

                content = f"""😋 「{topic}」真的绝了！

家人们谁懂啊！这个{topic}真的香迷糊了！

{taste}的味道浓郁，{dish}好吃到爆炸！

人均100+吃到扶墙出，性价比超高！

按头安利给所有吃货朋友！"""
            else:
                # 情感类轻松内容
                emotion = random.choice(topic_data.get("emotions", ["兴奋"]))
                action = random.choice(topic_data.get("actions", ["经历"]))

                content = f"""😍 关于「{topic}」有太多话要说！

那种{emotion}的感觉真的上头！

{action}的时候心跳加速到不行！

现在想想还是会忍不住微笑呢～

总之就是一整个青春回忆杀！"""
        except:
            content = f"""😄 「{topic}」太棒了！

这个体验真的绝绝子！让人超级开心！

推荐给所有小伙伴们！

绝对值得一试！"""

        return content

    def _generate_philosophical(self, topic, topic_data, keywords, is_food):
        """生成深度思考"""
        try:
            if is_food:
                # 美食类深度思考
                taste = random.choice(topic_data.get("tastes", ["美味"]))

                content = f"""💭 「{topic}」：饮食文化的思考

{topic}不仅是一种味觉享受，更是一种情感载体。

在{taste}的刺激中，人们卸下伪装，回归真实。

围坐一桌的亲密，分享食物的温暖。

美食的包容性，如同人际关系的一种隐喻。

一顿美食，一次情感的交流，一场生活的仪式。"""
            else:
                # 情感类深度思考
                emotion = random.choice(topic_data.get("emotions", ["情感"]))
                insight = random.choice(topic_data.get("insights", ["价值"]))

                content = f"""💭 「{topic}」：关于情感的思考

{topic}不仅是一种情感体验，更是个体与世界关系的镜像。

在{emotion}的情感投射中，我们看到的究竟是对方，还是自我理想的倒影？

从哲学角度看，{topic}是个体面对虚无时的情感创造。

在不确定的世界中，我们通过情感投入来确认自身的{insight}和价值。"""
        except:
            content = f"""💭 「{topic}」：深度思考

{topic}不仅是一种体验，更是一种生命的感悟。

它让我们思考存在的意义，体会生命的价值。

在{topic}的过程中，我们与自我对话，与世界连接。

这就是{topic}的哲学意义所在。"""

        return content


# ---------- 初始化 ----------
generator = SmartGenerator()

# ---------- 主界面 ----------
# 主题输入
st.subheader("🎯 创作主题")
topic = st.text_input(
    "请输入您的创作主题",
    value="重庆火锅探店",
    placeholder="例如：学生时代的暗恋、烧烤店体验、旅行回忆",
    help="支持美食、情感、旅行、读书等主题"
)

# 智能关键词推荐
if topic:
    recommended_keywords = generator.get_recommended_keywords(topic)
    recommended_str = "、".join(recommended_keywords[:8])

    st.subheader("🔑 关键词设置")

    col1, col2 = st.columns([3, 1])

    with col1:
        # 关键词输入框
        user_keywords = st.text_input(
            "输入关键词（用逗号分隔）",
            placeholder="例如：麻辣、毛肚、服务、环境",
            help="可以输入自己的关键词，或使用下方推荐"
        )

    with col2:
        # 使用推荐按钮
        if st.button("使用推荐", key="use_recommend"):
            # 更新session state
            st.session_state.recommended_keywords = ",".join(recommended_keywords[:5])
            st.rerun()

    # 如果用户点击了推荐按钮
    if "recommended_keywords" in st.session_state:
        user_keywords = st.session_state.recommended_keywords
        st.success(f"✅ 已使用推荐关键词：{st.session_state.recommended_keywords}")

    # 显示推荐关键词
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
    horizontal=True,
    format_func=lambda x: {
        "感性叙事": "💖 情感细腻",
        "理性分析": "📊 客观理性",
        "专业测评": "⭐️ 专业评测",
        "轻松活泼": "😄 活泼有趣",
        "深度思考": "💭 深度哲学"
    }[x]
)

# 内容长度 - 添加了超短文案选项
st.subheader("📏 内容长度")
length = st.radio(
    "选择内容长度",
    ["超短文案", "短篇精简", "标准长度", "详细长文"],
    horizontal=True,
    index=1,
    format_func=lambda x: {
        "超短文案": "📌 10字以内",
        "短篇精简": "📄 10-50字",
        "标准长度": "📄📄 50-200字",
        "详细长文": "📄📄📄 200-300字"
    }[x]
)

# 生成按钮
if st.button("🚀 生成智能文案", type="primary", use_container_width=True):
    if not topic:
        st.warning("请输入创作主题")
    else:
        # 生成内容
        content = generator.generate_content(topic, style, length, user_keywords)
        word_count = len(content.replace(' ', '').replace('\n', ''))

        # 显示字数信息
        length_info = {
            "超短文案": "10字以内",
            "短篇精简": "10-50字",
            "标准长度": "50-200字",
            "详细长文": "200-300字"
        }

        # 生成标题
        title_styles = {
            "感性叙事": f"❤️ {topic}：藏在时光里的温暖记忆",
            "理性分析": f"📊 {topic}分析报告",
            "专业测评": f"⭐️ {topic}测评报告",
            "轻松活泼": f"😋 绝了！{topic}真的太上头了！",
            "深度思考": f"💭 {topic}：关于文化与情感的思考"
        }
        title = title_styles.get(style, f"{topic}体验分享")

        # 保存结果
        st.session_state.current_result = {
            "title": title,
            "content": content,
            "word_count": word_count,
            "style": style,
            "length": length,
            "length_info": length_info[length],
            "keywords": user_keywords if user_keywords else "使用智能推荐"
        }

# ---------- 显示结果 ----------
if "current_result" in st.session_state:
    result = st.session_state.current_result

    st.markdown("---")

    # 对于超短文案，显示更大的字体
    if result['length'] == "超短文案":
        st.markdown(f"# 🎯 超短文案")
        st.markdown(f"## {result['content']}")
    else:
        st.markdown(f"# {result['title']}")

    # 信息卡片
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("📝 当前字数", f"{result['word_count']}字")
    with col2:
        st.metric("🎯 目标范围", result['length_info'])
    with col3:
        st.metric("🎨 风格", result['style'])
    with col4:
        # 显示关键词
        if result['keywords']:
            kw_display = result['keywords'].split(',')[0]
            if len(result['keywords'].split(',')) > 1:
                kw_display += " 等"
            st.metric("🔑 关键词", kw_display)

    # 字数状态指示
    st.markdown("---")

    # 根据实际字数给出反馈
    actual_length = result['word_count']
    if result['length'] == "超短文案":
        if actual_length <= 10:
            st.success(f"✅ 完美！超短文案（{actual_length}字）")
        else:
            st.warning(f"⚠️ 当前字数{actual_length}字，略超出10字限制")
    elif result['length'] == "短篇精简":
        target_range = (10, 50)
        if actual_length < target_range[0]:
            st.warning(f"⚠️ 当前字数偏少（{actual_length}字）")
        elif actual_length > target_range[1]:
            st.warning(f"⚠️ 当前字数偏多（{actual_length}字）")
        else:
            st.success(f"✅ 字数符合预期（{actual_length}字）")
    elif result['length'] == "标准长度":
        target_range = (50, 200)
        if actual_length < target_range[0]:
            st.warning(f"⚠️ 当前字数偏少（{actual_length}字）")
        elif actual_length > target_range[1]:
            st.warning(f"⚠️ 当前字数偏多（{actual_length}字）")
        else:
            st.success(f"✅ 字数符合预期（{actual_length}字）")
    else:  # 详细长文
        target_range = (200, 300)
        if actual_length < target_range[0]:
            st.warning(f"⚠️ 当前字数偏少（{actual_length}字）")
        elif actual_length > target_range[1]:
            st.warning(f"⚠️ 当前字数偏多（{actual_length}字）")
        else:
            st.success(f"✅ 字数符合预期（{actual_length}字）")

    st.markdown("---")

    # 显示内容（超短文案已经显示过了，这里显示普通内容）
    if result['length'] != "超短文案":
        st.markdown(result['content'])

    # 复制功能
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

# ---------- 侧边栏 ----------
with st.sidebar:
    st.markdown("## 📖 使用说明")

    st.markdown("""
    ### 🎯 创作主题示例

    **美食探店**：
    - 重庆火锅探店
    - 日式烧烤体验  
    - 咖啡店打卡分享

    **情感心理**：
    - 学生时代的暗恋
    - 失恋成长经历
    - 友谊的故事

    **其他主题**：
    - 旅行游记分享
    - 读书心得体会
    - 职场成长经历

    ### 🔑 关键词功能

    1. **智能推荐**：
       - 系统根据主题自动推荐
       - 点击"使用推荐"按钮

    2. **自定义输入**：
       - 输入自己的关键词
       - 用逗号分隔

    3. **智能融合**：
       - 关键词会自然融入内容
       - 避免生硬插入

    ### 🎨 风格特点

    - **💖 感性叙事**：情感细腻，故事性强
    - **📊 理性分析**：客观冷静，逻辑清晰  
    - **⭐️ 专业测评**：详细打分，专业视角
    - **😄 轻松活泼**：幽默风趣，网络用语
    - **💭 深度思考**：哲学思考，深层分析

    ### 📏 内容长度说明

    - **📌 超短文案**：10字以内，适合广告语、口号
    - **📄 短篇精简**：10-50字，适合微博、朋友圈
    - **📄📄 标准长度**：50-200字，适合公众号、小红书
    - **📄📄📄 详细长文**：200-300字，适合深度内容
    """)

    st.markdown("---")
    st.success("✅ **智能文案生成器**\n\n• 支持超短文案生成\n• 智能关键词推荐\n• 多种写作风格\n• 精准字数控制")
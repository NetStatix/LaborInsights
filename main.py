import streamlit as st
import pandas as pd
import plotly.express as px
import altair as alt
import plotly.graph_objects as go
import os
from dotenv import load_dotenv
load_dotenv()

BASE_DIR = os.getenv("BASE_DIR")

st.set_page_config(
    page_title="Հայկական աշխատաշուկայի վերլուծություն",
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="📊"
)


st.markdown("""
<style>
    :root {
        --primary: #D90026;  /* Armenian red */
        --secondary: #0033A0;  /* Armenian blue */
        --accent: #F2A900;  /* Armenian orange */
        --dark: #0E1117;
        --light: #FAFAFA;
        --gray: #AAAAAA;
    }
    
    .main {
        background: linear-gradient(135deg, #0E1117 0%, #1A1D24 100%);
    }
    
    .header-container {
        background: linear-gradient(90deg, var(--dark) 0%, var(--primary) 100%);
        padding: 2rem;
        border-radius: 0 0 15px 15px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.3);
        margin-bottom: 2rem;
    }
    
    .header-title {
        color: var(--light);
        font-size: 2.8rem;
        font-weight: 500;
        margin-bottom: 0.5rem;
    }
    
    .header-subtitle {
        color: var(--gray);
        font-size: 2.6rem;
        font-weight: 700;
        margin-bottom: 0;
    }
    
    .metric-card {
        background: rgba(30, 30, 30, 0.7);
        border-radius: 10px;
        padding: 1.5rem;
        border-left: 4px solid var(--primary);
        transition: all 0.3s ease;
    }
    
    .metric-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 20px rgba(0,0,0,0.2);
    }
    
    .metric-title {
        color: var(--gray);
        font-size: 1rem;
        margin-bottom: 0.5rem;
    }
    
    .metric-value {
        color: var(--light);
        font-size: 1.5rem;
        font-weight: 700;
    }
    
    .stExpander {
        background: rgba(30, 30, 30, 0.7) !important;
        border-radius: 10px !important;
        border: 1px solid #333 !important;
    }
    
    .stExpander > summary {
        font-size: 1.2rem !important;
        font-weight: 600 !important;
        color: var(--light) !important;
    }
    
    .footer {
        background: linear-gradient(90deg, var(--dark) 0%, var(--secondary) 100%);
        padding: 2rem;
        border-radius: 15px;
        margin-top: 2rem;
    }
    
    .footer-title {
        color: var(--light);
        font-size: 1.5rem;
        margin-bottom: 1rem;
    }
    
    .footer-text {
        color: var(--gray);
        font-size: 1rem;
    }
    
    .cta-link {
        color: var(--accent) !important;
        font-weight: 600;
        transition: all 0.2s ease;
    }
    
    .cta-link:hover {
        color: var(--primary) !important;
        text-decoration: none;
    }
    
    /* Hide Streamlit default elements */
    #MainMenu {visibility: hidden;}
    .stDeployButton {display:none;}
    footer {visibility: hidden;}
    #stDecoration {display:none;}
</style>
""", unsafe_allow_html=True)


translations = {
    "hy": {
        "page_title": "Հայկական աշխատաշուկայի վերլուծություն",
        "welcome_title": "Հայկական աշխատաշուկայի վերլուծություն",
        "welcome_text1": "Այս հարթակում կգտնեք հայկական աշխատաշուկայի առաջատար ոլորտները , պահանջված մասնագիտությունները , հմտությունները և այլ կարևոր վիճակագրական տվյալներ ։",
        "welcome_text2": "Վերլուծությունները կազմված են Staff.am-ի կողմից հրապարակված աշխատանքային հայտարարությունների հիման վրա և ներկայացնում են հետաքրքիր վիճակագրություն աշխատաշուկայի վիճակի մասին ։ Ներկայացված վերլուծությունները հնարավորություն են տալիս գործատուներին և մասնագետներին գնահատել աշխատաշուկայի առաջարկն ու պահանջարկը՝ ապահովելով ապագա քայլերի ռազմավարական և արդյունավետ պլանավորում ։",

        "top_metrics_overview_title": "Ստորև ներկայացված են հայկական աշխատաշուկայի առաջատար ինդուստրիան , աշխատանքային կատեգորիան , աշխատանքը և հմտությունը ․",

        

        "select_display_mode": "Ընտրել ցուցադրման ձևը",
        "show_count": "Ցուցադրել քանակը",
        "show_percent": "Ցուցադրել տոկոսը",


        "industry_title":"Գրաֆիկում ներկայացաված են Հայաստանի աշխատաշուկայի թոփ ինդուստրիաները.",
        "category_title":"Գրաֆիկում ներկայացաված են Հայաստանի աշխատաշուկայի թոփ աշխատանքային կատեգորիաները. ",
        "companies_title":"Գրաֆիկում ներկայացաված են Հայաստանի աշխատաշուկայի թոփ գործատուները. ",
        "jobs_title":"Գրաֆիկում ներկայացաված են Հայաստանի աշխատաշուկայի թոփ հաստիքների ցանկը. ",
        "positions_title":"Գրաֆիկում ներկայացաված են Հայաստանի աշխատաշուկայի թոփ ընդհանուր մասնագիտական ուղղվածություն ունեցող մասնագետների ցանկը.",
        "skills_title":"Գրաֆիկում ներկայացաված են Հայաստանի աշխատաշուկայի թոփ մասնագիտական հմտությունները. ",
        "skills_title_8":"Գրաֆիկում ներկայացաված են Հայաստանի աշխատաշուկայի թոփ փափուկ հմտությունները. ",

        "levels_title":"Գրաֆիկում ներկայացաված են Հայաստանի աշխատաշուկայի մասնագիտական մակարդակների բաշխվածությունը. ",
        "employments_title":"Գրաֆիկում ներկայացաված են Հայաստանի աշխատաշուկայի աշխատանքային պայմանագրի տեսակների բաշխվածությունը. ",

        "sidebar_header": "Ֆիլտր և կարգավորում",
        "sidebar_topn": "Թոփ արդյունքների քանակը",
        "sidebar_expanders": "Բաժինները բաց/փակ վիճակում",
        "total_jobs": "Ընդհանուր թափուր հաստիքներ",
        "Թոփ ինդուստրիա": "Թոփ ինդուստրիա",
        "Թոփ կատեգորիա": "Թոփ կատեգորիա",
        "companies": "Թոփ ընկերություններ",
        "Թոփ աշխատանք": "Թոփ աշխատանք",
        "Թոփ հմտություն": "Թոփ հմտություն",
        "Թոփ ինդուստրիաներ ըստ թափուր հաստիքների": "Թոփ ինդուստրիաներն ըստ թափուր հաստիքների",
        "industries": "Թոփ ինդուստրիաներ",
        "categories": "Թոփ կատեգորիաներ",
        "jobs": "Թոփ աշխատանքներ",
        "jobss": "Թոփ հաստիքներ",
        "skills": "Թոփ հմտություններ",
        "top_categories_by_vacancies": "Թոփ {n} կատեգորիաներ ըստ թափուր հաստիքների",

      
        "level_distribution": "Լեվելների բաշխվածություն",
        "employment_terms_distribution": "Աշխատանքի պայմանների բաշխվածություն",

        "Աշխատանքային պայմանների հակիրճ վերլուծություն": "Աշխատանքային պայմանների հակիրճ վերլուծություն",
        "analyze_prompt": "Անցեք այս հղումներով՝ տեսնելու ավելին",
        "go_to_companies": "Անցնել «Ընկերություններ» բաժին",
        "go_to_industries": "Անցնել «Ինդուստրիաներ» բաժին",
        "go_to_categories": "Անցնել «Կատեգորիաներ» բաժին",
        "go_to_jobs": "Անցնել «Աշխատանքներ» բաժին",
        "go_to_levels": "Անցնել «Մակարդակներ» բաժին",
        
    },
"en": {
  "page_title": "Armenian Labor Market Analysis",
  "welcome_title": "Armenian Labor Market Analysis",
  "welcome_text1": "Here you’ll find the leading industries, in-demand roles, skills, and other key indicators of the Armenian labor market.",
  "welcome_text2": "The analyses are based on job advertisements published by Staff.am and present interesting statistics about the state of the labor market. The presented analyses enable employers and professionals to assess labor market supply and demand, ensuring strategic and effective planning of future steps.",
  "top_metrics_overview_title": "Below are the leading industry, job category, job title, and skill in the Armenian labor market.",

  
  "select_display_mode": "Choose display mode",
  "show_count": "Show count",
  "show_percent": "Show percent",

  "industry_title": "The chart shows the top industries in Armenia’s labor market.",
  "category_title": "The chart shows the top job categories in Armenia’s labor market.",
  "companies_title": "The chart shows the top employers in Armenia’s labor market.",
  "jobs_title": "The chart shows the top job titles in Armenia’s labor market.",
  "positions_title": "The chart shows the top occupational categories (general professional directions).",
  "skills_title": "The chart shows the top professional skills in Armenia’s labor market.",
  "skills_title_8": "The chart shows the top soft skills in Armenia’s labor market.",

  "levels_title": "The chart shows the distribution of professional levels in Armenia’s labor market.",
  "employments_title": "The chart shows the distribution of employment terms in Armenia’s labor market.",

  "sidebar_header": "Filters & settings",
  "sidebar_topn": "Number of top results",
  "sidebar_expanders": "Sections open/closed",
  "total_jobs": "Total open positions",

  "Թոփ ինդուստրիա": "Top industry",
  "Թոփ կատեգորիա": "Top category",
  "companies": "Top companies",
  "Թոփ աշխատանք": "Top job",
  "Թոփ հմտություն": "Top skill",
  "Թոփ ինդուստրիաներ ըստ թափուր հաստիքների": "Top industries by open positions",

  "industries": "Top industries",
  "categories": "Top categories",
  "jobs": "Top jobs",
  "jobss": "Top positions",
  "skills": "Top skills",
  "top_categories_by_vacancies": "Top {n} categories by open positions",

  "level_distribution": "Level distribution",
  "employment_terms_distribution": "Employment terms distribution",

  "Աշխատանքային պայմանների հակիրճ վերլուծություն": "Quick analysis of employment terms",
  "analyze_prompt": "Use the links below to explore more",
  "go_to_companies": "Go to “Companies”",
  "go_to_industries": "Go to “Industries”",
  "go_to_categories": "Go to “Categories”",
  "go_to_jobs": "Go to “Jobs”",
  "go_to_levels": "Go to “Levels”"
},

"ru": {
  "page_title": "Аналитика рынка труда Армении",
  "welcome_title": "Аналитика рынка труда Армении",
  "welcome_text1": "Здесь вы найдёте ведущие отрасли, востребованные должности, навыки и другие ключевые показатели рынка труда Армении.",
  "welcome_text2":" «Анализ основан на объявлениях о вакансиях, опубликованных Staff.am, и содержит интересную статистику о состоянии рынка труда.Представленные анализы позволяют работодателям и специалистам оценивать спрос и предложение на рынке труда, обеспечивая стратегическое и эффективное планирование будущих шагов.",
  "top_metrics_overview_title": "Ниже представлены лидирующие отрасль, категория, должность и навык на рынке труда Армении.",

  

  "select_display_mode": "Выберите режим отображения",
  "show_count": "Показать количество",
  "show_percent": "Показать долю (%)",

  "industry_title": "На графике показаны топ-отрасли рынка труда Армении.",
  "category_title": "На графике показаны топ-категории вакансий рынка труда Армении.",
  "companies_title": "На графике показаны топ-работодатели рынка труда Армении.",
  "jobs_title": "На графике показаны топ-должности рынка труда Армении.",
  "positions_title": "На графике показаны топ профессиональных направлений (обобщённых категорий).",
  "skills_title": "На графике показаны топ профессиональных навыков рынка труда Армении.",
  "skills_title_8": "На графике показаны топ soft-skills рынка труда Армении.",

  "levels_title": "Распределение профессиональных уровней на рынке труда Армении.",
  "employments_title": "Распределение типов занятости на рынке труда Армении.",

  "sidebar_header": "Фильтр и настройки",
  "sidebar_topn": "Количество топ-результатов",
  "sidebar_expanders": "Разделы (открыть/закрыть)",
  "total_jobs": "Всего открытых позиций",

  "Թոփ ինդուստրիա": "Топ-отрасль",
  "Թոփ կատեգորիա": "Топ-категория",
  "companies": "Топ компании",
  "Թոփ աշխատանք": "Топ-должность",
  "Թոփ հմտություն": "Топ-навык",
  "Թոփ ինդուստրիաներ ըստ թափուր հաստիքների": "Топ-отрасли по числу открытых позиций",

  "industries": "Топ-отрасли",
  "categories": "Топ-категории",
  "jobs": "Топ-должности",
  "jobss": "Топ-позиции",
  "skills": "Топ-навыки",
  "top_categories_by_vacancies": "Топ {n} категорий по числу вакансий",

  "level_distribution": "Распределение уровней",
  "employment_terms_distribution": "Распределение условий занятости",

  "Աշխատանքային պայմանների հակիրճ վերլուծություն": "Краткий анализ условий занятости",
  "analyze_prompt": "Перейдите по ссылкам ниже, чтобы посмотреть больше",
  "go_to_companies": "Перейти в «Компании»",
  "go_to_industries": "Перейти в «Отрасли»",
  "go_to_categories": "Перейти в «Категории»",
  "go_to_jobs": "Перейти в «Должности»",
  "go_to_levels": "Перейти в «Уровни»"
},  
}

if "lang" not in st.session_state:
    st.session_state["lang"] = "EN" 

lang_choice = st.sidebar.selectbox("🌐 Choose language", ['HY', 'EN', 'RU'], 
                                   index=['HY', 'EN', 'RU'].index(st.session_state["lang"].upper()))

st.session_state["lang"] = lang_choice.lower()

lang = st.session_state["lang"]


st.markdown(f"""
<div class="header-container">
    <h3 class="header-title">{translations[lang]["welcome_title"]}</h3>
    <p class="header-subtitle">{translations[lang]["welcome_text1"]}</p>
    <p class="header-subtitle">{translations[lang]["welcome_text2"]}</p>


</div>
""", unsafe_allow_html=True)

@st.cache_data
def load_data(path=f"{BASE_DIR}data/All.xlsx"):
    df = pd.read_excel(path)
    df.columns = [col.lower() for col in df.columns]
    return df
df = load_data()

with st.sidebar:
    st.markdown(f"<h3 style='color:var(--light)'>{translations[lang]['sidebar_header']}</h3>", unsafe_allow_html=True)
    top_n = st.slider(translations[lang]["sidebar_topn"], min_value=5, max_value=15, value=10, key="top_n_slider")
    show_expanders = st.checkbox(translations[lang]["sidebar_expanders"], value=True, key="expander_checkbox")
    
    total_jobs = len(df)
    st.markdown(f"""
    <div style="background:rgba(30,30,30,0.7); padding:1rem; border-radius:10px; border-left:4px solid var(--secondary); margin-top:1rem;">
        <p style="color:var(--gray); margin:0; font-size:0.9rem;">{translations[lang]['total_jobs']}</p>
        <p style="color:var(--light); margin:0; font-size:1.5rem; font-weight:700;">{total_jobs:,}</p>
    </div>
    """, unsafe_allow_html=True)

industry_counts = df['industry'].value_counts(dropna=True)
top_industry = industry_counts.idxmax()
top_industry_count = industry_counts.max()
industry_percent = round(top_industry_count / len(df) * 100, 1)

category_counts = df['category'].value_counts(dropna=True)
top_category = category_counts.idxmax()
top_category_count = category_counts.max()
category_percent = round(top_category_count / len(df) * 100, 1)

job_counts = df['name'].value_counts(dropna=True)
top_job = job_counts.idxmax()
top_job_count = job_counts.max()
job_percent = round(top_job_count / len(df) * 100, 1)

skill_cols = [c for c in df.columns if c.startswith('professional_skills_')]
skill_series = df[skill_cols].stack().str.strip().dropna()
skill_counts = skill_series.value_counts()
top_skill = skill_counts.idxmax()
top_skill_count = skill_counts.max()
skill_percent = round(top_skill_count / skill_series.shape[0] * 100, 1)

st.markdown("---")
# ------------------------------------------------------------
def make_ring_chart_with_labels(percent, top_label, bottom_label, color="#00BFFF"):
    fig = go.Figure(data=[go.Pie(
        values=[percent, 100 - percent],
        hole=0.7,
        marker=dict(colors=[color, "#2C2C3C"]),
        textinfo="none"
    )])
    fig.update_layout(
        showlegend=False,
        paper_bgcolor="#1E1E2F",
        margin=dict(t=40, b=40, l=40, r=40),
        width=250,
        height=300
    )
    fig.add_annotation(
        text=f"{percent}%",
        x=0.5, y=0.5,
        font=dict(size=22, color="white"),
        showarrow=False
    )
    fig.add_annotation(
        text=f"<b>{top_label}</b>",
        x=0.5, y=1.1,
        xref="paper", yref="paper",
        font=dict(size=16, color="white"),
        showarrow=False
    )
   
    fig.add_annotation(
        text=f"{bottom_label}",
        x=0.5, y=-0.05,
        xref="paper", yref="paper",
        font=dict(size=14, color="lightgray"),
        showarrow=False
    )
    return fig


# ------------------------------------------------------------
st.markdown(
    f"""
    <div style='font-size:20px; font-weight:bold; color:#d8e2eb;'>
        {translations[lang]['top_metrics_overview_title']}
    </div>
    """,
    unsafe_allow_html=True
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.plotly_chart(make_ring_chart_with_labels(industry_percent, "Top Industry", top_industry, "#00BFFF"), use_container_width=True)

with col2:
    st.plotly_chart(make_ring_chart_with_labels(category_percent, "Top Category", top_category, "#FF5733"), use_container_width=True)

with col3:
    st.plotly_chart(make_ring_chart_with_labels(job_percent, "Top Job Title", top_job, "#28B463"), use_container_width=True)

with col4:
    st.plotly_chart(make_ring_chart_with_labels(skill_percent, "Top Skill", top_skill, "#AF7AC5"), use_container_width=True)

st.markdown("---")
name5 = "industry"

def plot_top_industries(df, top_n=10, key_suffix=""):
    st.markdown(f"<p>{translations[lang]['industry_title']}</p>", unsafe_allow_html=True)

    options = {
        "count": translations[lang]["show_count"],
        "percent": translations[lang]["show_percent"]
    }

   
    uniq = f"{lang}_{name5}"
    if key_suffix:
        uniq += f"_{key_suffix}"

    display_mode = st.selectbox(
        translations[lang]["select_display_mode"],
        options.keys(),
        format_func=lambda x: options[x],
        key=f"display_mode_{uniq}"     
    )

   
    industry_counts = (
        df["industry"].dropna().astype(str).str.strip().replace("", None).dropna()
        .value_counts().head(top_n).rename_axis("Industry").reset_index(name="Open positions")
    )
    total = industry_counts["Open positions"].sum()
    percentages = (industry_counts["Open positions"] / total * 100).round(1)

    if display_mode == "count":
        y_data = industry_counts["Open positions"]
        text_data = industry_counts["Open positions"].astype(str)
        y_title = "Open Positions (number)"
        hovertpl = "<b>%{x}</b><br>Open positions: %{y}<extra></extra>"
        yaxis_cfg = dict(title=y_title, gridcolor="rgba(255,255,255,0.1)")
    else:
        y_data = percentages
        text_data = percentages.map(lambda p: f"{p:.1f}%")
        y_title = "Open Positions (percent)"
        hovertpl = "<b>%{x}</b><br>Share: %{y:.1f}%<extra></extra>"
        yaxis_cfg = dict(title=y_title, ticksuffix="%", gridcolor="rgba(255,255,255,0.1)")

    fig = px.bar(
        industry_counts,
        x="Industry",
        y=y_data,
        color=y_data,
        color_continuous_scale="Viridis",
        text=text_data,
        height=550
    )
    fig.update_traces(
        textposition="outside",
        marker_line_color="white",
        marker_line_width=1,
        hovertemplate=hovertpl
    )
    fig.update_layout(
        showlegend=False,
        coloraxis_showscale=False,  
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(color="white"),
        margin=dict(t=60, b=60, l=60, r=40),
        xaxis=dict(
            title=None,
            tickangle=-45,
            categoryorder="array",
            categoryarray=industry_counts["Industry"].tolist(),
            showgrid=False
        ),
        yaxis=yaxis_cfg
    )
    return fig

#-----------------------------------------------------------------------------------------------------
def plot_top_categories(df, top_n=10):
    st.markdown(f"<p>{translations[lang]['category_title']}</p>", unsafe_allow_html=True)

    category_counts = (
        df['category']
        .dropna()
        .value_counts()
        .head(top_n)
        .reset_index()
    )
    category_counts.columns = ['Category', 'Open Positions']

    fig = px.pie(
        category_counts,
        names='Category',
        values='Open Positions',
        color='Open Positions',
        color_discrete_sequence=px.colors.sequential.Purples,
        hole=0.3
    )

    fig.update_traces(
        textinfo='percent',
        textposition='inside',
        pull=[0.05]*len(category_counts),
        marker=dict(line=dict(color='#000000', width=2.5)),
        showlegend=True
    )

    fig.update_layout(
        margin=dict(t=50, b=50, l=50, r=50),
        legend=dict(
            orientation="h",        
            y=-0.2,                 
            x=0.5,
            xanchor="center",
            font=dict(size=14)
        )
    )

    return fig
    
#---------------------------------------------------------------------------------------
name4 = "companies"

def plot_top_companies(df, top_n=10, key_suffix=""):
    if 'company' not in df.columns:
        st.warning(translations[lang].get("company_missing_warning", "Company data not available"))
        return None

    st.markdown(f"<p>{translations[lang]['companies_title']}</p>", unsafe_allow_html=True)

    options = {
        "count": translations[lang]["show_count"],
        "percent": translations[lang]["show_percent"]
    }

    uniq = f"{lang}_{name4}"
    if key_suffix:
        uniq += f"_{key_suffix}"

    display_mode = st.selectbox(
        translations[lang]["select_display_mode"],
        options.keys(),
        format_func=lambda x: options[x],
        key=f"display_mode_{uniq}"
    )

    company_counts = (
        df['company'].dropna()
          .astype(str).str.strip()
          .replace('', None).dropna()
          .value_counts()
          .head(top_n)
          .rename_axis('Company')
          .reset_index(name='Open positions')
    )
    total = company_counts['Open positions'].sum()
    company_counts['Percentage'] = (company_counts['Open positions'] / total * 100).round(1)

    if display_mode == "count":
        y_data = company_counts['Open positions']
        text_data = company_counts['Open positions'].astype(str)
        y_title = translations[lang].get("open_positions", "Open Positions (number)")
        hovertpl = "<b>%{y}</b><br>Open positions: %{x}<extra></extra>"
        yaxis_cfg = dict(title=y_title, gridcolor='rgba(255,255,255,0.1)')
    else:
        y_data = company_counts['Percentage']
        text_data = company_counts['Percentage'].map(lambda p: f"{p:.1f}%")
        y_title = "Open Positions (percent)"
        hovertpl = "<b>%{y}</b><br>Share: %{x:.1f}%<extra></extra>"
        yaxis_cfg = dict(title=y_title, ticksuffix="%", gridcolor='rgba(255,255,255,0.1)')

    fig = px.bar(
        company_counts,
        x='Company',                    
        y=y_data,                      
        color=y_data,
        color_continuous_scale='sunset',
        text=text_data,
        height=max(420, 60 + 28 * len(company_counts))
)

    fig.update_traces(
        textposition='outside',
        textfont_size=12,
        marker_line_color='white',
        marker_line_width=1.2,
        hovertemplate=hovertpl,
        showlegend=False
    )

    fig.update_layout(
    showlegend=False,
    coloraxis_showscale=False,  
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    font=dict(color='white'),
    yaxis=yaxis_cfg,
    xaxis=dict(
        title=None,       
        tickfont=dict(size=12)
    ),
    margin=dict(t=60, b=60, l=60, r=40),
    height=500
)

    return fig

name2 = "bla"

def plot_top_jobs_by(df, top_n=10, key_suffix=""):
    if 'jobcategorybyfirst' not in df.columns:
        st.warning("Job category data not available")
        return None

    st.markdown(f"<p>{translations[lang]['positions_title']}</p>", unsafe_allow_html=True)

    options = {
        "count": translations[lang]["show_count"],
        "percent": translations[lang]["show_percent"]
    }

    uniq = f"{lang}_{name2}"
    if key_suffix:
        uniq += f"_{key_suffix}"

    display_mode = st.selectbox(
        translations[lang]["select_display_mode"],
        options.keys(),
        format_func=lambda x: options[x],
        key=f"display_mode_{uniq}"
    )

    job_counts = (
        df['jobcategorybyfirst']
          .dropna()
          .astype(str).str.strip()
          .replace('', None).dropna()
          .value_counts()
          .head(top_n)
          .rename_axis('Job Title')
          .reset_index(name='Open positions')
    )

    total = job_counts['Open positions'].sum()
    job_counts['Percentage'] = (job_counts['Open positions'] / total * 100).round(1)

    if display_mode == "count":
        x_data = job_counts['Open positions']
        text_data = job_counts['Open positions'].astype(str)
        x_title = "Open Positions (number)"
        hovertpl = "<b>%{y}</b><br>Open positions: %{x}<extra></extra>"
        xaxis_cfg = dict(title=x_title, gridcolor='rgba(255,255,255,0.1)', zerolinecolor='rgba(255,255,255,0.3)')
    else:
        x_data = job_counts['Percentage']
        text_data = job_counts['Percentage'].map(lambda p: f"{p:.1f}%")
        x_title = "Open Positions (percent)"
        hovertpl = "<b>%{y}</b><br>Share: %{x:.1f}%<extra></extra>"
        xaxis_cfg = dict(title=x_title, ticksuffix="%", gridcolor='rgba(255,255,255,0.1)', zerolinecolor='rgba(255,255,255,0.3)')

    fig = px.bar(
    job_counts,
    x='Job Title',               
    y=x_data,                    
    color=x_data,
    color_continuous_scale='tealrose',
    text=text_data,
    height=max(420, 60 + 28 * len(job_counts))
)

    fig.update_traces(
    textposition='outside',
    textfont_size=12,
    textfont_color='white',
    marker_line_color='white',
    marker_line_width=1.2,
    hovertemplate=hovertpl,
    showlegend=False
)

    fig.update_layout(
    showlegend=False,
    coloraxis_showscale=False, 
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    font=dict(color='white', family="Arial", size=12),
    xaxis=dict(
        title='',                 
        tickfont=dict(size=12),
        tickangle=-45,          
        gridcolor='rgba(255,255,255,0.1)'
    ),
    yaxis=xaxis_cfg,
    margin=dict(t=60, b=120, l=40, r=40),
    height = 550
)

    return fig


name3 = "jobs"

def plot_top_jobs(df, top_n=10, key_suffix=""):
    if 'name' not in df.columns:
        return None

    st.markdown(f"<p>{translations[lang]['jobs_title']}</p>", unsafe_allow_html=True)

    options = {
        "count": translations[lang]["show_count"],
        "percent": translations[lang]["show_percent"]
    }

    uniq = f"{lang}_{name3}"
    if key_suffix:
        uniq += f"_{key_suffix}"

    display_mode = st.selectbox(
        translations[lang]["select_display_mode"],
        options.keys(),
        format_func=lambda x: options[x],
        key=f"display_mode_{uniq}"
    )

    job_counts = (
        df['name']
          .dropna()
          .astype(str).str.strip()
          .replace('', None).dropna()
          .value_counts()
          .head(top_n)
          .rename_axis('Job Title')
          .reset_index(name='Open positions')
    )
    total = job_counts['Open positions'].sum()
    job_counts['Percentage'] = (job_counts['Open positions'] / total * 100).round(1)

    if display_mode == "count":
        x_data = job_counts["Open positions"]
        text_data = job_counts["Open positions"].astype(str)
        x_title = translations[lang].get("open_positions", "Open Positions (number)")
        hovertpl = "<b>%{y}</b><br>Open positions: %{x}<extra></extra>"
        xaxis_cfg = dict(title=x_title, gridcolor='rgba(255,255,255,0.1)', zerolinecolor='rgba(255,255,255,0.3)')
    else:
        x_data = job_counts["Percentage"]
        text_data = job_counts["Percentage"].map(lambda p: f"{p:.1f}%")
        x_title = "Open Positions (percent)"
        hovertpl = "<b>%{y}</b><br>Share: %{x:.1f}%<extra></extra>"
        xaxis_cfg = dict(title=x_title, ticksuffix="%", gridcolor='rgba(255,255,255,0.1)', zerolinecolor='rgba(255,255,255,0.3)')

    fig = px.bar(
    job_counts,
    x='Job Title',           
    y=x_data,                
    color=x_data,
    color_continuous_scale='deep',
    text=text_data,
    hover_data={'Job Title': True},
    height=max(420, 60 + 28 * len(job_counts))
)

    fig.update_traces(
        textposition='outside',
        textfont_size=12,
        textfont_color='white',
        marker_line_color='white',
        marker_line_width=1.5,
        hovertemplate=hovertpl,
        showlegend=False
    )

    fig.update_layout(
        showlegend=False,
        coloraxis_showscale=False,  
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white', family="Arial", size=12),
        xaxis=dict(
            title='',
            tickangle=-45,          
            tickfont=dict(size=12),
            gridcolor='rgba(255,255,255,0.1)'
        ),
        yaxis=xaxis_cfg,
        margin=dict(t=60, b=120, l=40, r=40),
        height = 500
    )


    return fig

name1 = "skills"

def plot_top_skills(df, top_n=10, key_suffix=""):
    skill_cols = [f'professional_skills_{i}' for i in range(1, 11) if f'professional_skills_{i}' in df.columns]
    if not skill_cols:
        return None

    st.markdown(f"<p>{translations[lang]['skills_title']}</p>", unsafe_allow_html=True)

    options = {
        "count": translations[lang]["show_count"],
        "percent": translations[lang]["show_percent"]
    }

    uniq = f"{lang}_{name1}"
    if key_suffix:
        uniq += f"_{key_suffix}"

    display_mode = st.selectbox(
        translations[lang]["select_display_mode"],
        options.keys(),
        format_func=lambda x: options[x],
        key=f"display_mode_{uniq}"
    )

  
    s = (
        df[skill_cols]
        .apply(lambda row: row.dropna().tolist(), axis=1)
        .explode()
        .dropna()
        .astype(str).str.strip()
        .replace('', None).dropna()
    )

    s_norm = s.str.lower()
    first_variant = s.groupby(s_norm).first()        
    counts = s_norm.value_counts().head(top_n)       

    skill_counts = (
        counts.rename_axis('norm')
              .reset_index(name='Count')
              .assign(Skill=lambda d: d['norm'].map(first_variant))
              [['Skill', 'Count']]
    )

    total = skill_counts['Count'].sum()
    skill_counts['Percentage'] = (skill_counts['Count'] / total * 100).round(1)

    if display_mode == "count":
        x_data = skill_counts["Count"]
        text_data = skill_counts["Count"].astype(str)
        x_title = "Number"
        hovertpl = "<b>%{y}</b><br>Count: %{x}<extra></extra>"
        xaxis_cfg = dict(title=x_title, gridcolor='rgba(255,255,255,0.1)', zerolinecolor='rgba(255,255,255,0.3)')
    else:
        x_data = skill_counts["Percentage"]
        text_data = skill_counts["Percentage"].map(lambda p: f"{p:.1f}%")
        x_title = "Percent"
        hovertpl = "<b>%{y}</b><br>Share: %{x:.1f}%<extra></extra>"
        xaxis_cfg = dict(title=x_title, ticksuffix="%", gridcolor='rgba(255,255,255,0.1)', zerolinecolor='rgba(255,255,255,0.3)')

    fig = px.bar(
    skill_counts,
    x='Skill',                 
    y=x_data,                  
    color=x_data,
    color_continuous_scale='Plasma',
    text=text_data,
    height=max(420, 60 + 28 * len(skill_counts))
)

    fig.update_traces(
        textposition='outside',
        textfont_size=12,
        textfont_color='white',
        marker_line_color='black',
        marker_line_width=0.5,
        hovertemplate=hovertpl,
        showlegend=False
)

    fig.update_layout(
        showlegend=False,
        coloraxis_showscale=False,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white', family='Arial', size=12),
        xaxis=dict(
            title='',
            tickangle=-45,   
            tickfont=dict(size=12),
            gridcolor='rgba(255,255,255,0.1)'
        ),
        yaxis=xaxis_cfg,
        margin=dict(t=60, b=120, l=40, r=40),
        height = 550
    )


    return fig

def plot_level_distribution(df):
    valid_levels = ['Student', 'Junior', 'Mid level', 'Senior', 'Not defined']
    if 'level' not in df.columns:
        return None
    
    st.markdown(f"""
    <p>{translations[lang]["levels_title"]}</p>
  
    """, unsafe_allow_html=True)
    level_counts = (
        df[df['level'].isin(valid_levels)]['level']
        .value_counts()
        .reindex(valid_levels, fill_value=0)
        .reset_index()
    )
    level_counts.columns = ['Level', 'Count']
    
    fig = px.pie(
        level_counts,
        names='Level',
        values='Count',
        color_discrete_sequence=px.colors.sequential.RdBu
    )
    
    fig.update_traces(
        textinfo='label+percent',
        textposition='outside',
        pull=[0.05] * len(level_counts),
        marker=dict(line=dict(color='#000000', width=1))
    )
    
    fig.update_layout(
        showlegend=False,
        margin=dict(t=50, b=50, l=50, r=50),
        uniformtext_minsize=12,
        uniformtext_mode='hide',
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font_color='white'
    )
    
    return fig
#---------------------------------------------------------------------------------
name8 = "skills8"

def plot_top_soft_skills(df, top_n=10, key_suffix=""):
    # Սյունակների ստուգում
    skill_cols = [f'personal_skills_{i}' for i in range(1, 11) if f'personal_skills_{i}' in df.columns]
    if not skill_cols:
        return None

    st.markdown(f"<p>{translations[lang]['skills_title_8']}</p>", unsafe_allow_html=True)

    
    options = {
        "count": translations[lang]["show_count"],
        "percent": translations[lang]["show_percent"]
    }

    uniq = f"{lang}_{name8}"
    if key_suffix:
        uniq += f"_{key_suffix}"

    display_mode = st.selectbox(
        translations[lang]["select_display_mode"],
        options.keys(),
        format_func=lambda x: options[x],
        key=f"display_mode_{uniq}"
    )

    s = (
        df[skill_cols]
        .apply(lambda row: row.dropna().tolist(), axis=1)
        .explode()
        .dropna()
        .astype(str).str.strip()
        .replace('', None).dropna()
    )

    s_norm = s.str.lower()
    first_variant = s.groupby(s_norm).first()       
    counts = s_norm.value_counts().head(top_n)      

    skill_counts = (
        counts.rename_axis('norm')
              .reset_index(name='Count')
              .assign(Skill=lambda d: d['norm'].map(first_variant))
              [['Skill', 'Count']]
    )

    total = skill_counts['Count'].sum()
    skill_counts['Percentage'] = (skill_counts['Count'] / total * 100).round(1)

    if display_mode == "count":
        x_data = skill_counts["Count"]
        text_data = skill_counts["Count"].astype(str)
        x_title = "Number"
        hovertpl = "<b>%{y}</b><br>Count: %{x}<extra></extra>"
        xaxis_cfg = dict(title=x_title, gridcolor='rgba(255,255,255,0.1)', zerolinecolor='rgba(255,255,255,0.3)')
    else:
        x_data = skill_counts["Percentage"]
        text_data = skill_counts["Percentage"].map(lambda p: f"{p:.1f}%")
        x_title = "Percent"
        hovertpl = "<b>%{y}</b><br>Share: %{x:.1f}%<extra></extra>"
        xaxis_cfg = dict(title=x_title, ticksuffix="%", gridcolor='rgba(255,255,255,0.1)', zerolinecolor='rgba(255,255,255,0.3)')

    fig = px.bar(
    skill_counts,
    x='Skill',               
    y=x_data,                 
    color=x_data,
    color_continuous_scale='Plasma',
    text=text_data,
    height=max(420, 60 + 28 * len(skill_counts))
)

    fig.update_traces(
        textposition='outside',
        textfont_size=12,
        textfont_color='white',
        marker_line_color='black',
        marker_line_width=0.5,
        hovertemplate=hovertpl,
        showlegend=False
)

    fig.update_layout(
        showlegend=False,
        coloraxis_showscale=False,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white', family='Arial', size=12),
        xaxis=dict(
            title='',
            tickangle=-45,  
            tickfont=dict(size=12),
            gridcolor='rgba(255,255,255,0.1)'
        ),
        yaxis=xaxis_cfg,
        margin=dict(t=60, b=120, l=40, r=40),
        height = 550
)
    return fig
#---------------------------------------------------------------


name_emp = "employment_term"

def plot_employment_terms(df, lang, top_n=None, key_suffix=""):
    cols = {str(c).strip().lower(): c for c in df.columns}
    if "employment term" not in cols:
        st.warning("Employment term data not available")
        return None
    col = cols["employment term"]

    st.markdown(f"<p>{translations[lang]['employments_title']}</p>", unsafe_allow_html=True)

    options = {"count": translations[lang]["show_count"], "percent": translations[lang]["show_percent"]}
    uniq = f"{lang}_{name_emp}" + (f"_{key_suffix}" if key_suffix else "")
    display_mode = st.selectbox(
        translations[lang]["select_display_mode"],
        options.keys(),
        format_func=lambda x: options[x],
        key=f"display_mode_{uniq}"
    )

    emp_counts = (
        df[col].dropna()
               .astype(str).str.strip()
               .replace("", None).dropna()
               .value_counts()
               .rename_axis("Employment Term")
               .reset_index(name="Count")
    )
    if top_n:
        emp_counts = emp_counts.head(top_n)

    emp_counts["Percentage"] = (emp_counts["Count"] / emp_counts["Count"].sum() * 100).round(1)

    if display_mode == "count":
        y_vals = emp_counts["Count"]
        text_vals = emp_counts["Count"].astype(str)
        yaxis_cfg = dict(title="Open Positions (number)",
                         gridcolor="rgba(255,255,255,0.2)",
                         zerolinecolor="rgba(255,255,255,0.3)")
        hovertpl = "<b>%{x}</b><br>Count: %{y}<extra></extra>"
    else:
        y_vals = emp_counts["Percentage"]
        text_vals = emp_counts["Percentage"].map(lambda p: f"{p:.1f}%")
        yaxis_cfg = dict(title="Open Positions (percent)", ticksuffix="%",
                         gridcolor="rgba(255,255,255,0.2)",
                         zerolinecolor="rgba(255,255,255,0.3)")
        hovertpl = "<b>%{x}</b><br>Share: %{y:.1f}%<extra></extra>"

    fig = px.bar(
        emp_counts,
        x="Employment Term",
        y=y_vals,
        color=y_vals,
        color_continuous_scale="teal",
        text=text_vals,
        height=max(420, 60 + 28 * len(emp_counts))
    )

    fig.update_traces(
        textposition="outside",
        textfont=dict(color="white", size=12),
        marker_line_color="white",
        marker_line_width=1.2,
        hovertemplate=hovertpl,
        showlegend=False
    )

    fig.update_layout(
        showlegend=False,
        coloraxis_showscale=False,        
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(color="white"),
        margin=dict(t=60, b=120, l=40, r=40),  
        xaxis=dict(
            title="",
            tickangle=-45,
            tickfont=dict(size=12),
            categoryorder="total descending",  
            showgrid=True,
            gridcolor="rgba(255,255,255,0.2)"
        ),
        yaxis=yaxis_cfg,
        hoverlabel=dict(bgcolor="rgba(0,0,0,0.8)", font_size=12),
        height = 550
    )
    return fig

   

def render_expander(title, plot_func, df, top_n=None, **kwargs):
    with st.expander(title, expanded=show_expanders):
        with st.spinner("🔄 Բեռնվում է..."):
            fig = plot_func(df, top_n, **kwargs) if top_n is not None else plot_func(df, **kwargs)
            if fig:
                if isinstance(fig, alt.Chart):
                    st.altair_chart(fig, use_container_width=True)
                else:
                    st.plotly_chart(fig, use_container_width=True)


render_expander(f"📈 {translations[lang]['industries']} ({top_n})", plot_top_industries, df, top_n)
render_expander(f"📦 {translations[lang]['categories']} ({top_n})", plot_top_categories, df, top_n)
render_expander(f"🏭 {translations[lang]['companies']} ({top_n})", plot_top_companies, df, top_n)
render_expander(f"👔 {translations[lang]['jobss']} ({top_n})", plot_top_jobs_by, df, top_n)
render_expander(f"💼 {translations[lang]['jobs']} ({top_n})", plot_top_jobs, df, top_n)
render_expander(f"🛠️ {translations[lang]['skills']} ({top_n})", plot_top_skills, df, top_n)
render_expander(f"🛠️ {translations[lang]['skills']} ({top_n})", plot_top_soft_skills, df, top_n)
render_expander(f"🎯 {translations[lang]['level_distribution']}", plot_level_distribution, df)
render_expander(f"📊 {translations[lang]['employment_terms_distribution']}", plot_employment_terms, df, lang=lang)


st.markdown(f"""
<div style="background-color:rgba(30,30,30,0.7); padding:2rem; border-radius:10px; margin-top:2rem; border-left:4px solid var(--accent);">
    <h3 style="color:var(--light); margin-top:0;">{translations[lang]["analyze_prompt"]}</h3>
    <ul style="color:var(--light);">
        <li>➡️ <a href="/Industries" target="_self" class="cta-link">{translations[lang]["go_to_industries"]}</a></li>
        <li>➡️ <a href="/Categories" target="_self" class="cta-link">{translations[lang]["go_to_categories"]}</a></li>
        <li>➡️ <a href="/Companies" target="_self" class="cta-link">{translations[lang]["go_to_companies"]}</a></li>
        <li>➡️ <a href="/Jobs" target="_self" class="cta-link">{translations[lang]["go_to_jobs"]}</a></li>
        <li>➡️ <a href="/Levels" target="_self" class="cta-link">{translations[lang]["go_to_levels"]}</a></li>
    </ul>
</div>
""", unsafe_allow_html=True)


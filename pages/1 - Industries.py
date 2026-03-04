import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
from dotenv import load_dotenv
load_dotenv()
import os
BASE_DIR = os.getenv("BASE_DIR")
st.set_page_config(
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="📊"
)
lang = st.session_state.get("lang", "hy")

translations = {

"hy": {
    "industry_page_title": "Ինդուստրիաների վերլուծություն",

    "top_industries": "Թոփ 10 ինդուստրիաները",
       
    "title": "Ինդուստրիաների բաշխվածությունն ըստ մակարդակների",

    "finance_title": "Հայաստանում Finance / Banking / Insurance ոլորտի դերը",
        "finance_data": """
          
          - **Finance / Banking / Insurance** ոլորտը կազմում է Հայաստանի աշխատաշուկայի **27.7%-ը**։
          - Այն զբաղեցնում է աշխատաշուկայի գրեթե **1/3** մասը, ինչն ընդգծում է ֆինանսական ոլորտի գերակշռող դերը։  
        """,
        "finance_conclusion": """
        Հայաստանում ֆինանսական ոլորտը համարվում է ամենաարագ զարգացող և ակտիվ ոլորտներից մեկը։ Այն բացում է նոր հնարավորություններ մասնագետների համար՝ ապահովելով զարգացման և երկարաժամկետ կարիերայի կառուցման պայմաններ։
         
        """,
    "conclusion_title":"Եզրակացություն",
    "select_level": "Ընտրել մակարդակը ․",
    "select_industry": "Ընտրել ինդուստրիան ․",

    "no_data": "Տվյալներ չեն գտնվել այս մակարդակի համար։",

    "about_industry":"Ինդուստրիաների գնահատումն ըստ տարբեր ցուցանիշների",

    "prof_skills_by_level": "Մասնագիտական հմտություններն ըստ մակարդակի",

    "level_button_prompt": "Ընտրել մակարդակը հմտությունները դիտելու համար․",

    "no_level_data": "Տվյալներ չկան ընտրված մակարդակի համար։",

    "no_skills_for_filter": "Հմտությունների տվյալներ չկան ընտրված մակարդակի համար։",

    "top_skills_by_level": "Պահանջվող հմտությունները {industry} ոլորտում «{level}» մակարդակում",

    "top_15_skills_chart_title": "Մասնագիտական հմտություններ «{level}» մակարդակի համար ",

    "top_10_companies_title": "🏢 Թոփ 10 գործատուները «{industry}» ինդուստրիայում ",
    "companies_chart_x": "Կազմակերպություն",
    "companies_chart_y": "Թափուր հաստիքներ",

    "level_distribution_title": "Մակարդակների բաշխվածությունը «{industry}» ինդուստրիայում ",

    "top_15_skills_industry": "💼 Թոփ 15 մասնագիտական հմտությունները «{industry}» ինդուստրիայի համար",

    "top_10_jobs_title": "📝 Թոփ 10 հաստիքները «{industry}» ինդուստրիայում ",
    "top_10_jobs_chart_title": "Թոփ 10 աշխատանքները «{industry}» ինդուստրիայի համար",
    "job_column": "Աշխատանք",
    "open_positions_column": "Թափուր հաստիքների քանակ",
    "missing_level_column": "Level սյունը բացակայում է տվյալների մեջ։",
    "missing_job_column": "'name' սյունակը բացակայում է տվյալների մեջ։",
    "no_skills_for_filter": "Հմտությունների տվյալներ չկան ընտրված ֆիլտրի համար։",
    "no_data_for_level": "Տվյալներ չկան ընտրված լեվելի համար։",
},
"en": {
  "industry_page_title": "Job Industries Analysis",

  "top_industries": "Top 10 industries",

  "title": "Industry distribution by levels.",

  "finance_title": "The role of Finance / Banking / Insurance in Armenia",
  "finance_data": " - **Finance / Banking / Insurance** accounts for **27.7%** of Armenia’s labor market.\n - It covers almost **one-third** of the market, highlighting the dominant role of the financial sector.",
  "finance_conclusion": "In Armenia, the financial sector is among the fastest-growing and most active domains. It opens new opportunities for professionals, enabling development and long-term career building.",

  "conclusion_title": "Conclusion",
  "select_level": "Select level",
  "select_industry": "Select industry",

  "no_data": "No data found for this level.",

  "about_industry": "Industry evaluation by various indicators.",
  "prof_skills_by_level": "Professional skills by level.",
  "level_button_prompt": "Select a level to view the skills.",
  "no_level_data": "No data for the selected level.",
  "no_skills_for_filter": "No skills data for the selected filter.",

  "top_skills_by_level": "Required skills in {industry} at `{level}` level",
  "top_15_skills_chart_title": "Professional skills for `{level}` level.",

  "top_10_companies_title": "🏢 Top 10 employers in the “{industry}” industry.",
  "companies_chart_x": "Company",
  "companies_chart_y": "Open positions",

  "level_distribution_title": "Level distribution in the `{industry}` industry.",

  "top_15_skills_industry": "💼 Top 15 professional skills for the `{industry}` industry.",

  "top_10_jobs_title": "📝 Top 10 jobs in the `{industry}` industry.",
  "top_10_jobs_chart_title": "Top 10 jobs for the `{industry}` industry",
  "job_column": "Job",
  "open_positions_column": "Number of open positions",
  "missing_level_column": "The 'level' column is missing from the data.",
  "missing_job_column": "The 'name' column is missing from the data.",
  "no_data_for_level": "No data for the selected level."
},
"ru": {
  "industry_page_title": "Аналитика отраслей",

  "top_industries": "Топ-10 отраслей",

  "title": "Распределение отраслей по уровням.",

  "finance_title": "Роль Finance / Banking / Insurance в Армении",
  "finance_data": " - Сектор **Finance / Banking / Insurance** составляет **27.7%** рынка труда Армении.\n - Это почти **треть** рынка, что подчёркивает доминирующую роль финансовой сферы.",
  "finance_conclusion": "Финансовый сектор в Армении — один из самых быстрорастущих и активных. Он открывает новые возможности для специалистов, обеспечивая условия для развития и построения долгосрочной карьеры.",

  "conclusion_title": "Вывод",
  "select_level": "Выберите уровень",
  "select_industry": "Выберите отрасль",

  "no_data": "Данные для этого уровня не найдены.",

  "about_industry": "Оценка отраслей по различным показателям.",
  "prof_skills_by_level": "Профессиональные навыки по уровням.",
  "level_button_prompt": "Выберите уровень, чтобы посмотреть навыки.",
  "no_level_data": "Нет данных для выбранного уровня.",
  "no_skills_for_filter": "Нет данных по навыкам для выбранного фильтра.",

  "top_skills_by_level": "Требуемые навыки в отрасли {industry} на уровне `{level}`",
  "top_15_skills_chart_title": "Профессиональные навыки для уровня `{level}`.",

  "top_10_companies_title": "🏢 Топ-10 работодателей в отрасли «{industry}».",
  "companies_chart_x": "Компания",
  "companies_chart_y": "Открытые позиции",

  "level_distribution_title": "Распределение уровней в отрасли «{industry}».",

  "top_15_skills_industry": "💼 Топ-15 профессиональных навыков для отрасли «{industry}».",

  "top_10_jobs_title": "📝 Топ-10 должностей в отрасли «{industry}».",
  "top_10_jobs_chart_title": "Топ-10 должностей для отрасли «{industry}»",
  "job_column": "Должность",
  "open_positions_column": "Количество открытых позиций",
  "missing_level_column": "В данных отсутствует столбец 'level'.",
  "missing_job_column": "В данных отсутствует столбец 'name'.",
  "no_data_for_level": "Нет данных для выбранного уровня."
}
}


st.markdown(f"""
<div style="
        background: linear-gradient(90deg, #0f172a 0%, #64748b 100%);
        padding: 2rem;
        border-radius: 15px;
        margin-top: 2rem;
        color: white;
        font-size: 2.2rem;
        line-height: 1.6;
        text-align: center;
">
    {translations[lang]["industry_page_title"]}
</div>
""", unsafe_allow_html=True)

st.markdown("""
<style>
.subheader-industry{
  font-size: 25px;        
  font-weight: 700;
  color: #d8e2eb;
  line-height: 1.2;
  margin: .25rem 0 1rem 0;
}
</style>
""", unsafe_allow_html=True)

# --- Load Data ---
@st.cache_data
def load_data(path=f"{BASE_DIR}data/All.xlsx"):
    df = pd.read_excel(path)
    df.columns = [col.lower() for col in df.columns]
    return df

df = load_data()


t = translations[lang]

# --- Թոփ 10 ինդուստրիաները ընդհանուր շուկայում
with st.container():
    st.markdown("---")
    st.subheader(t["top_industries"])

    top_industries = df["industry"].dropna().value_counts().head(10)

    fig = px.bar(
        x=top_industries.values,
        y=top_industries.index,
        orientation="h",
        labels={"x": "count", "y": "company"},
        color=top_industries.values,
        color_continuous_scale="Blues"
    )

    fig.update_layout(
        yaxis_title=None,
        xaxis_title="Open Positions (number)",
        height=500
    )

    st.plotly_chart(fig, use_container_width=True)
    top_industry = top_industries.index[0]
    percentage = top_industries.iloc[0] / top_industries.sum() * 100

    second_industry = top_industries.index[1]
    second_percentage = top_industries.iloc[1] / top_industries.sum() * 100

st.markdown("---")

with st.container():
    st.markdown(f"### {translations[lang]['finance_title']}")
    st.markdown(translations[lang]['finance_data'])

    st.markdown(
        f"""
        <div style="
            background: linear-gradient(90deg, #0f172a 0%, #64748b 100%);
            padding: 1.5rem;
            border-radius: 15px;
            margin-top: 1rem;
            color: white;
            font-size: 1.2rem;
            line-height: 1.6;
        ">
            📌 <b>{translations[lang]['conclusion_title']}</b><br><br>
            {translations[lang]['finance_conclusion']}
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("---") 

available_levels = ['Student', 'Junior', 'Mid level', 'Senior', 'Not defined']

st.markdown(f"<div class='subheader-industry'> {translations[lang]['title']}</div>", unsafe_allow_html=True)

st.markdown(f"{t['select_level']}")
cols = st.columns(len(available_levels))
active_level = None

for idx, level in enumerate(available_levels):
    if cols[idx].button(level, key=f"industry_level_{idx}"):
        active_level = level

if active_level:
    filtered_df = df[df["level"] == active_level]

    if filtered_df.empty:
        st.warning(t["no_data"])
    else:
        top_industries_filtered = (
            filtered_df["industry"]
            .value_counts()
            .nlargest(10)
            .sort_values(ascending=True)
        )

        fig, ax = plt.subplots()
        top_industries_filtered.plot(kind="barh", ax=ax, color="skyblue")
        ax.set_xlabel("Open Positions (number)")
        ax.set_ylabel("Industry")
        ax.set_title(f"{t['title']} ({active_level})")
        st.pyplot(fig)

df = df.dropna(subset=["industry", "company"])

st.markdown("---")
st.markdown(f"<div class='subheader-industry'> {translations[lang]['about_industry']}</div>", unsafe_allow_html=True)


# Ինդուստրիայի ընտրություն
industries = df['industry'].dropna().unique()
selected_industry = st.selectbox(translations[lang]["select_industry"], sorted(industries))

# Ֆիլտրում ըստ ինդուստրիայի
filtered_df = df[df["industry"] == selected_industry]

skill_columns = [f"professional_skills_{i}" for i in range(1, 11)]

# --- Բլոկ 1: Մասնագիտական հմտություններ ըստ լեվելի կոճակներով ---
with st.container():
    st.markdown(
        f"""
        <div style='
            border:1px solid #cccccc;
            padding:15px;
            border-radius:8px;
            margin-bottom:20px;'>
        """,
        unsafe_allow_html=True
    )
    st.markdown(f"<div class='subheader-industry'> {translations[lang]['prof_skills_by_level']}</div>", unsafe_allow_html=True)
    
    st.info(translations[lang]["level_button_prompt"])

    available_levels = ['Student', 'Junior', 'Mid level', 'Senior', 'Not defined']
    cols = st.columns(5)
    active_level = None

    for idx, level in enumerate(available_levels):
        if cols[idx].button(level):
            active_level = level

    if active_level:
        level_filtered_df = filtered_df[filtered_df['level'] == active_level]

        if not level_filtered_df.empty:
            all_skills = level_filtered_df[skill_columns].apply(lambda x: x.dropna().tolist(), axis=1).explode()
            skill_counts = all_skills.value_counts().reset_index()
            skill_counts.columns = ['Skill', 'Color']

            if not skill_counts.empty:
                top_skills = skill_counts.head(15)

                st.markdown(translations[lang]["top_skills_by_level"].format(industry=selected_industry, level=active_level))


                fig_skills = px.bar(
                    top_skills,
                    x='Skill',
                    y='Color',
                    color='Color',
                    color_continuous_scale='Magma',
                    # title=f"Թոփ 15 մասնագիտական հմտություններ `{active_level}` մակարդակի համար"
                )
                fig_skills.update_layout(
                    xaxis_title=None,
                    yaxis_title="Number",
                    # title_x=0.5
                )
                st.plotly_chart(fig_skills, use_container_width=True)

                st.dataframe(top_skills, hide_index=True, use_container_width=True)
            else:
                st.info(translations[lang]["no_skills_for_filter"])
        else:
            st.warning(translations[lang]["no_data_for_level"])

    st.markdown("</div>", unsafe_allow_html=True)

# --- Բլոկ 2: Թոփ 10 կազմակերպություններ ---
with st.container():
    st.markdown(
        f"""
        <div style='
            border:1px solid #cccccc;
            padding:15px;
            border-radius:8px;
            margin-bottom:20px;'>
        """,
        unsafe_allow_html=True
    )
    st.markdown(f"<div class='subheader-industry'> {translations[lang]['top_10_companies_title'].format(industry=selected_industry)}</div>", unsafe_allow_html=True)
    
    top_companies = (
        filtered_df["company"]
        .value_counts()
        .head(10)
        .reset_index()
    )
    top_companies.columns = ["Company", "Color"]

    fig = px.bar(
        top_companies,
        x="Company",
        y="Color",
        color="Color",
        color_continuous_scale="blues",
        text="Color",
        title = "Distribution of companies"
    )
    fig.update_layout(xaxis_title=None, yaxis_title="Open Positions (number)", title_x=0.5 , height = 600)
    fig.update_traces(textposition="outside")

    st.plotly_chart(fig, use_container_width=True)

    st.markdown("</div>", unsafe_allow_html=True)

# --- Բլոկ 3: Լեվելների բաշխվածություն ---
with st.container():
    st.markdown(
        f"""
        <div style='
            border:1px solid #cccccc;
            padding:15px;
            border-radius:8px;
            margin-bottom:20px;'>
        """,
        unsafe_allow_html=True
    )
    st.markdown(f"<div class='subheader-industry'> {translations[lang]['level_distribution_title'].format(industry=selected_industry)}</div>", unsafe_allow_html=True)

    allowed_levels = ['Student', 'Junior', 'Mid level', 'Senior', 'Not defined']

    if 'level' in filtered_df.columns:
        filtered_levels_df = filtered_df[filtered_df['level'].isin(allowed_levels)]
        level_counts = (
            filtered_levels_df['level']
            .value_counts()
            .reindex(allowed_levels, fill_value=0)
            .reset_index()
        )
        level_counts.columns = ['level', 'Color']

        fig_levels = px.bar(
            level_counts,
            x='level',
            y='Color',
            color="Color",
            color_continuous_scale='blues',
            title="Distribution of levels"
        )
        fig_levels.update_layout(xaxis_title=None, yaxis_title="Open Positions (number)", title_x=0.5)
        st.plotly_chart(fig_levels, use_container_width=True)
    else:
        st.warning("Level սյունը բացակայում է տվյալների մեջ։")

    st.markdown("</div>", unsafe_allow_html=True)

# --- Բլոկ 4: Թոփ 15 հմտություններ ըստ ինդուստրիայի ---
with st.container():
    st.markdown(
        f"""
        <div style='
            border:1px solid #cccccc;
            padding:15px;
            border-radius:8px;
            margin-bottom:20px;'>
        """,
        unsafe_allow_html=True
    )
    st.markdown(f"<div class='subheader-industry'> {translations[lang]['top_15_skills_industry'].format(industry=selected_industry)}</div>", unsafe_allow_html=True)

    all_skills = filtered_df[skill_columns].apply(lambda x: x.dropna().tolist(), axis=1).explode()
    skill_counts = all_skills.value_counts().reset_index()
    skill_counts.columns = ['Skill', 'Color']
    top_skills = skill_counts.head(15)

    fig_skills = px.bar(
        top_skills,
        x='Skill',
        y='Color',
        color="Color",
        color_continuous_scale='Plasma',
        title="Distribution of skills",
        
    )
    fig_skills.update_layout(xaxis_title=None, yaxis_title="Open Positions (number)" , title_x=0.5)
    st.plotly_chart(fig_skills, use_container_width=True)

    st.markdown("</div>", unsafe_allow_html=True)

# --- Բլոկ 5: Թոփ 10 աշխատանքներ ---
with st.container():
    st.markdown(
        f"""
        <div style='
            border:1px solid #cccccc;
            padding:15px;
            border-radius:8px;
            margin-bottom:20px;'>
        """,
        unsafe_allow_html=True
    )
    st.markdown(f"<div class='subheader-industry'> {translations[lang]['top_10_jobs_title'].format(industry=selected_industry)}</div>", unsafe_allow_html=True)

if "name" in filtered_df.columns:
    job_counts = (
        filtered_df["name"]
        .dropna()
        .astype(str).str.strip()
        .replace("", None).dropna()
        .value_counts()
        .head(10)
        .reset_index()
    )
    job_counts.columns = ["Job Title", "Color"]  

    def wrap_tick(s: str, width: int = 20) -> str:
        words = str(s).split()
        lines, cur = [], ""
        for w in words:
            if len(cur) + len(w) + 1 > width:
                if cur:
                    lines.append(cur)
                cur = w
            else:
                cur = (cur + " " + w).strip()
        if cur:
            lines.append(cur)
        return "<br>".join(lines)

    job_counts["Job Title Wrapped"] = job_counts["Job Title"].apply(lambda x: wrap_tick(x, 20))

    fig_jobs = px.bar(
        job_counts,
        x="Color",                         
        y="Job Title Wrapped",            
        orientation="h",
        color="Color",
        color_continuous_scale="Viridis",
        text="Color"
    )

    fig_jobs.update_traces(
        textposition="outside",
        textfont_size=12,
        marker_line_color="white",
        marker_line_width=1,
        showlegend=False,
        hovertemplate="<b>%{y}</b><br>Number: %{x}<extra></extra>"
    )

    fig_jobs.update_layout(
        coloraxis_showscale=False,         
        xaxis=dict(
            title="Open Positions (number)",
            gridcolor="rgba(255,255,255,0.12)",
            zerolinecolor="rgba(255,255,255,0.25)"
        ),
        yaxis=dict(
            title="",                      
            categoryorder="total ascending",
            tickfont=dict(size=12),
            automargin=True
        ),
        margin=dict(t=40, b=30, l=60, r=30),  
        height=520,
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(color="white")
    )

    st.plotly_chart(fig_jobs, use_container_width=True)
else:
    st.warning("❗ 'name' սյունակը բացակայում է տվյալների մեջ։")

    st.markdown("</div>", unsafe_allow_html=True)


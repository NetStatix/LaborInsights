import streamlit as st
import pandas as pd
import plotly.express as px
from collections import Counter

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
    "page_title": "Աշխատանքային կատեգորիաների վերլուծություն",

    "top_categories": "Թոփ 10 աշխատնքային կատեգորիաները",
    "top_category_analysis": " Հայաստանի աշխատաշուկայի առաջատար աշխատանքային կատեգորիան ներկայումս <b>{top_category}</b>-ն է, որը կազմում է մոտ <b>{percentage:.1f}%</b>։<br>Այս ցուցանիշը վկայում է <b>{top_category}</b> ոլորտում մասնագետների նկատմամբ բարձր պահանջարկի մասին և ստեղծում է կարիերայի լայն հնարավորություններ։",

    "top_levels": "Թոփ 10 մակարդակները",

    "title": "Աշխատանքային կատեգորիաներ բաշխվածությունն ըստ մակարդակների ",
        "select_level": "Ընտրել մակարդակը ․",
        "no_data": "Այս մակարդակի համար տվյալներ չկան։",


    "select_category": "Աշխատանքային կատեգորիաների գնահատումն ըստ տարբեր ցուցանիշների ",
    "select_category1":"Ընտրել աշխատանքային կատեգորիան ․",
    "skills_by_level": " Մասնագիտական հմտություններն ըստ մակարդակի ",

    "select_level_info": "Ընտրել մակարդակ հմտությունները դիտելու համար ․",
    "no_level_data": "Տվյալներ չկան ընտրված մակարդակի համար։",
    "no_skill_data": "Հմտությունների տվյալներ չկան ընտրված ֆիլտրի համար։",

    "top_skills_title": "✅ «{category}» կատեգորիայի {level} մակարդակի պահանջվող հմտությունները ",
    # "skills_chart_title": "Պահանջվող մասնագիտական հմտություններ {level} մակարդակի համար ․",

    "top_companies_title": "🏢 Թոփ 10 գործատուները «{category}» կատեգորիայում ",

    "levels_distribution": "🎯 Մակարդակների բաշխվածությունը «{category}» կատեգորիայում ",
    # "levels_chart_title": "Մակարդակների բաշխվածությունն ըստ թափուր հաստիքների ․",

    "top_skills_category": "💼 Թոփ 15 հմտությունները «{category}» կատեգորիայի համար ",

    "top_jobs_title": "📝 Թոփ 10 մասնագետները «{category}» կատեգորիայում ",

    "no_level_column": "Level սյունակը բացակայում է տվյալների մեջ։",
    "no_job_column": "'name' սյունակը բացակայում է տվյալների մեջ։",

},
"en": {
  "page_title": "Job Categories Analysis",

  "top_categories": "Top 10 job categories",
  "top_category_analysis": "The current leading job category in Armenia’s labor market is <b>{top_category}</b>, accounting for about <b>{percentage:.1f}%</b>.<br>This indicates strong demand for professionals in <b>{top_category}</b> and creates broad career opportunities.",

  "top_levels": "Top 10 levels",

  "title": "Distribution of job categories by levels",
  "select_level": "Select level",
  "no_data": "No data for this level.",

  "select_category": "Evaluation of job categories by various indicators",
  "select_category1": "Select a job category",
  "skills_by_level": "Professional skills by level",

  "select_level_info": "Select a level to view the skills",
  "no_level_data": "No data for the selected level.",
  "no_skill_data": "No skills data for the selected filter.",

  "top_skills_title": "✅ Required skills for {level} level in the “{category}” category",
#   "skills_chart_title": "Required professional skills for {level} level",

  "top_companies_title": "🏢 Top 10 employers in the “{category}” category",

  "levels_distribution": "🎯 Level distribution in the “{category}” category",
#   "levels_chart_title": "Level distribution by open positions",

  "top_skills_category": "💼 Top 15 skills for the “{category}” category",

  "top_jobs_title": "📝 Top 10 specialists in the “{category}” category",

  "no_level_column": "The 'level' column is missing from the data.",
  "no_job_column": "The 'name' column is missing from the data."
},
"ru": {
  "page_title": "Аналитика категорий вакансий",

  "top_categories": "Топ-10 категорий вакансий",
  "top_category_analysis": "На рынке труда Армении на данный момент лидирующая категория — <b>{top_category}</b>, на неё приходится около <b>{percentage:.1f}%</b>.<br>Это свидетельствует о высоком спросе на специалистов в области <b>{top_category}</b> и открывает широкие карьерные возможности.",

  "top_levels": "Топ-10 уровней",

  "title": "Распределение категорий по уровням",
  "select_level": "Выберите уровень",
  "no_data": "Нет данных для этого уровня.",

  "select_category": "Оценка категорий вакансий по различным показателям",
  "select_category1": "Выберите категорию вакансий",
  "skills_by_level": "Профессиональные навыки по уровням",

  "select_level_info": "Выберите уровень, чтобы посмотреть навыки",
  "no_level_data": "Нет данных для выбранного уровня.",
  "no_skill_data": "Нет данных по навыкам для выбранного фильтра.",

  "top_skills_title": "✅ Требуемые навыки для уровня {level} в категории «{category}»",
#   "skills_chart_title": "Требуемые профессиональные навыки для уровня {level}",

  "top_companies_title": "🏢 Топ-10 работодателей в категории «{category}»",

  "levels_distribution": "🎯 Распределение уровней в категории «{category}»",
#   "levels_chart_title": "Распределение уровней по числу открытых позиций",

  "top_skills_category": "💼 Топ-15 навыков для категории «{category}»",

  "top_jobs_title": "📝 Топ-10 специалистов в категории «{category}»",

  "no_level_column": "В данных отсутствует столбец 'level'.",
  "no_job_column": "В данных отсутствует столбец 'name'."
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
    {translations[lang]["page_title"]}
</div>
""", unsafe_allow_html=True)


st.markdown("---")
# --- Load Data ---
@st.cache_data
def load_data(path=f"{BASE_DIR}data/All.xlsx"):
    df = pd.read_excel(path)
    df.columns = [col.lower() for col in df.columns]
    return df

df = load_data()

st.markdown("""
<style>
.subheader-custom{
  font-size: 25px;        
  font-weight: 700;
  color: #d8e2eb;
  line-height: 1.2;
  margin: .25rem 0 1rem 0;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
.subheader-title{
  font-size: 15px;        
  font-weight: 700;
  color: #d8e2eb;
  line-height: 1.2;
  margin: .25rem 0 1rem 0;
}
</style>
""", unsafe_allow_html=True)

with st.container():
    st.markdown(f"<div class='subheader-custom'>{translations[lang]['top_categories']}</div>", unsafe_allow_html=True)

    # Թոփ 10 կատեգորիաները
    top_categories = df['category'].dropna().value_counts().head(10)

    fig = px.bar(
        x=top_categories.values,
        y=top_categories.index,
        orientation="h",
        labels={"x": "Number", "y": "name"},
        color=top_categories.values,
        color_continuous_scale="Blues"
    )

    fig.update_layout(
        yaxis_title=None,
        xaxis_title="Open Positions(number)",
        height=500
    )

    st.plotly_chart(fig, use_container_width=True, key="top_categories_bar")

    top_category = top_categories.index[0]
    percentage = top_categories.iloc[0] / top_categories.sum() * 100

    st.markdown(f"""
<div style="
    background-color:#3a6e9d;
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #D1C4E9;
    font-size: 16px;
    color: white;
    line-height: 1.6;">
{translations[lang]["top_category_analysis"].format(top_category=top_category, percentage=percentage)}
</div>
""", unsafe_allow_html=True)

st.markdown("---")
t = translations[lang]

available_levels = ['Student', 'Junior', 'Mid level', 'Senior', 'Not defined']

# --- Մակարդակ ընտրելու կոճակներ ---
st.markdown(f"""
<div style='font-size:30px; font-weight:bold; color:#d8e2eb;'>
    {translations[lang]["title"]}

</div>
""", unsafe_allow_html=True)

st.markdown(f"<div class='subheader-title'> {translations[lang]['select_level']}</div>", unsafe_allow_html=True)
cols = st.columns(len(available_levels))
active_level = None

for idx, level in enumerate(available_levels):
    if cols[idx].button(level, key=f"level_button_{idx}"):
        active_level = level

# --- Եթե ընտրություն կատարված է ---
if active_level:
    # ֆիլտրում ենք տվյալները ըստ մակարդակի
    filtered_df = df[df["level"] == active_level]

    if filtered_df.empty:
        st.warning(t["no_data"])
    else:
        # հաշվարկում ենք թոփ 10 կատեգորիաները
        top_categories = (
            filtered_df["category"]
            .value_counts()
            .nlargest(10)
            .sort_values(ascending=True)
        )

        fig, ax = plt.subplots()
        top_categories.plot(kind='barh', ax=ax, color='skyblue')
        ax.set_xlabel("Open Positions (number)")
        ax.set_ylabel("Category")
        ax.set_title(f"{t['title']} ({active_level})")
        st.pyplot(fig)

st.markdown("---")
df = df.dropna(subset=["category", "company"])

# Կատեգորիայի ընտրություն
st.markdown(f"""
<div style='font-size:30px; font-weight:bold; color:#d8e2eb;'>
    {translations[lang]["select_category"]}

</div>
""", unsafe_allow_html=True)
st.markdown(f"<div class='subheader-title'> {translations[lang]['select_category1']}</div>", unsafe_allow_html=True)


# selectbox առանց label-ի
categories = df['category'].dropna().unique()
selected_category = st.selectbox(
    "",
    sorted(categories),
    label_visibility="collapsed"
)
# Ֆիլտրում ըստ կատեգորիայի
filtered_df = df[df["category"] == selected_category]

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
    st.markdown(f"### {translations[lang]['skills_by_level']}") 
    st.markdown(f"<div class='subheader-title'> {translations[lang]['select_level_info']}</div>", unsafe_allow_html=True)

    available_levels = ['Student', 'Junior', 'Mid level', 'Senior', 'Not defined']
    cols = st.columns(5)
    active_level = None

    for idx, level in enumerate(available_levels):
        if cols[idx].button(level):
            active_level = level
 
    skill_columns = [f"professional_skills_{i}" for i in range(1, 11)]

    if active_level:
        level_filtered_df = filtered_df[filtered_df['level'] == active_level]

        if not level_filtered_df.empty:
            all_skills = level_filtered_df[skill_columns].apply(lambda x: x.dropna().tolist(), axis=1).explode()
            skill_counts = all_skills.value_counts().reset_index()
            skill_counts.columns = ['Skill', 'Color']

            if not skill_counts.empty:
                top_skills = skill_counts.head(15)

                st.markdown(translations[lang]["top_skills_title"].format(category=selected_category, level=active_level))


                fig_skills = px.bar(
                    top_skills,
                    x='Skill',
                    y='Color',
                    color='Color',
                    color_continuous_scale='Magma',
                    
                )
                fig_skills.update_layout(
                    xaxis_title=None,
                    yaxis_title="Number",
                    title_x=0.5
                )
                fig_skills.update_layout(title="Distribution of professional directions")

                st.plotly_chart(fig_skills, use_container_width=True)

                st.dataframe(top_skills, hide_index=True, use_container_width=True)
            else:
                st.info(translations[lang]["no_skill_data"])
        else:
            st.warning(translations[lang]["no_level_data"])
  


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
    st.markdown(f"<div class='subheader-custom'> {translations[lang]['top_companies_title'].format(category=selected_category)}</div>", unsafe_allow_html=True)

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
        title="Distribution of companies"
        

    )
    fig.update_layout(xaxis_title=None, yaxis_title="Open Positions (number)", title_x=0.5 , height =500)
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
    st.markdown(f"<div class='subheader-custom'> {translations[lang]['levels_distribution'].format(category=selected_category)}</div>", unsafe_allow_html=True)

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
            color='Color',
            color_continuous_scale='blues',
        )
        fig_levels.update_layout(xaxis_title=None, yaxis_title="Open Positions (number)", title_x=0.5)
        fig_levels.update_layout(title="Distribution of levels")

        st.plotly_chart(fig_levels, use_container_width=True)
    else:
        st.warning(translations[lang]["no_level_column"])

    st.markdown("</div>", unsafe_allow_html=True)


# --- Բլոկ 4: Թոփ 15 հմտություններ ըստ կատեգորիայի ---
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
    st.markdown(f"<div class='subheader-custom'>  {translations[lang]['top_skills_category'].format(category=selected_category)}</div>", unsafe_allow_html=True)

    all_skills = filtered_df[skill_columns].apply(lambda x: x.dropna().tolist(), axis=1).explode()
    skill_counts = all_skills.value_counts().reset_index()
    skill_counts.columns = ['Skill', 'Color']
    top_skills = skill_counts.head(15)

    fig_skills = px.bar(
        top_skills,
        x='Skill',
        y='Color',
        color='Color',
        color_continuous_scale='Plasma',
    )
    fig_skills.update_layout(xaxis_title=None, yaxis_title="Number")

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
    st.markdown(f"<div class='subheader-custom'> {translations[lang]['top_jobs_title'].format(category=selected_category)}</div>", unsafe_allow_html=True)

    if "name" in filtered_df.columns:
        job_counts = (
            filtered_df["name"]
            .dropna()
            .value_counts()
            .head(10)
            .reset_index()
        )
        job_counts.columns = ["Job Title", "Color"]

        fig_jobs = px.bar(
            job_counts,
            x="Job Title",                 
            y="Color",                     
            color="Color",
            color_continuous_scale="Viridis",
            text="Color",
            title="Distribution of specialists"
        )

        fig_jobs.update_traces(
            textposition="outside",
            textfont_size=12,
            showlegend=False,
            marker_line_color='white',
            marker_line_width=1
        )

        fig_jobs.update_layout(
            coloraxis_showscale=False,     
            xaxis=dict(
                title=translations[lang].get("job_column"),
                tickangle=-25,
                tickfont=dict(size=12),
                automargin=True,
                gridcolor='rgba(255,255,255,0.1)'
            ),
            yaxis=dict(
                title=translations[lang].get("open_positions_column", "Open Positions (number)"),
                tickfont=dict(size=12),
                gridcolor='rgba(255,255,255,0.12)',
                zerolinecolor='rgba(255,255,255,0.25)'
            ),
            margin=dict(t=60, b=120, l=70, r=30),
            title_x=0.3,
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(color='white'),
            height = 550
        )

        st.plotly_chart(fig_jobs, use_container_width=True)
    else:
        st.warning(translations[lang]["no_job_column"])


    st.markdown("</div>", unsafe_allow_html=True)

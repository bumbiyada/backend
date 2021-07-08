import pandas as pd
import plotly.graph_objs as go


""" File contains all scatters """


class Scatters:
    def __init__(self):
        pass

    @staticmethod
    def stage_user_bar(data):
        """ This scatter renders bars aff all done and not done tasks grouped by users """
        df_yes = pd.DataFrame(columns=['Stage_user', 'Is_done'])
        df_no = pd.DataFrame(columns=['Stage_user', 'Is_done'])
        df_2 = data.loc[:, 'Stage_user':'Is_done':2]
        for i in range(len(df_2)):
            done_var = df_2['Is_done'].iloc[i]
            user_var = df_2['Stage_user'].iloc[i]
            if done_var == 0:
                df_no = df_no.append({'Stage_user': user_var, 'Is_done': done_var}, ignore_index=True)
            elif done_var == 1:
                df_yes = df_yes.append({'Stage_user': user_var, 'Is_done': done_var}, ignore_index=True)
        sum_yes = df_yes['Stage_user'].value_counts()
        sum_no = df_no['Stage_user'].value_counts()
        sum_counts = data['Stage_user'].value_counts()

        list_my = sum_counts.index.to_list()
        list_my[0] = 'Исполнитель не указан'
        sum_counts.index = list_my

        fig = go.Figure()
        fig.add_trace(go.Bar(name='Выполнена', x=sum_yes.index, y=sum_yes))
        fig.add_trace(go.Bar(name='Не выполнена', x=sum_no.index, y=sum_no))
        fig.update_layout(
            legend_title_text="Задача Выполнена?",
            margin_l=30,
            margin_r=30,
            margin_t=20,
            margin_b=0,
            width=1400,
            barmode='stack')
        fig.update_yaxes(title_text="Количество выполненных задач")
        return fig

    @staticmethod
    def stage_name_pie(data):
        """ This scatter renders pie diagram of all tasks grouped by stage name """
        sum_counts_1 = data['Stage_name'].value_counts().sort_index()
        fig = go.Figure()
        fig.add_trace(go.Pie(values=sum_counts_1, labels=sum_counts_1.index, textinfo='label+percent'))
        fig.update_layout(
            legend_title_text="Этапы документа",
            margin_l=0,
            margin_r=0,
            margin_t=20,
            margin_b=0)
        return fig

    @staticmethod
    def is_aborted_pie(data):
        """ This scatter renders pie diagram of all tasks grouped by is_aborted(bool) """
        sum_counts = data['Is_aborted'].value_counts().sort_index()
        list_my = sum_counts.index.to_list()
        list_my[0] = 'нет'
        list_my[1] = 'да'
        sum_counts.index = list_my
        fig = go.Figure()
        fig.add_trace(go.Pie(values=sum_counts, labels=sum_counts.index, textinfo='label+percent'))
        fig.update_layout(
            legend_title_text="Задача отменена?",
            margin_l=0,
            margin_r=0,
            margin_t=20,
            margin_b=0)
        return fig

    @staticmethod
    def is_done_pie(data):
        """ This scatter renders pie diagram of all tasks grouped by is_done(bool) """
        sum_counts = data['Is_done'].value_counts().sort_index()
        list_my = sum_counts.index.to_list()
        list_my[0] = 'нет'
        list_my[1] = 'да'
        sum_counts.index = list_my
        fig = go.Figure()
        fig.add_trace(go.Pie(values=sum_counts, labels=sum_counts.index, textinfo='label+percent'))
        fig.update_layout(
            legend_title_text="задача выполнена?",
            margin_l=0,
            margin_r=0,
            margin_t=20,
            margin_b=0)
        return fig

    @staticmethod
    def marked_on_delete_pie(data):
        """ This scatter renders pie diagram of all tasks grouped by marked_on_delete(bool) """
        sum_counts = data['Marked_on_delete'].value_counts().sort_index()
        list_my = sum_counts.index.to_list()
        list_my[0] = 'нет'
        list_my[1] = 'да'
        sum_counts.index = list_my
        fig = go.Figure()
        fig.add_trace(go.Pie(values=sum_counts, labels=sum_counts.index, textinfo='label+percent'))
        fig.update_layout(
            legend_title_text="пометка на удаление",
            margin_l=0,
            margin_r=0,
            margin_t=20,
            margin_b=0)
        return fig

    @staticmethod
    def foiv_pie(data):
        """ This scatter renders pie diagram of all tasks grouped by Foiv """
        sum_counts = data['Foiv'].value_counts().sort_index()
        fig = go.Figure()
        fig.add_trace(go.Pie(values=sum_counts, labels=sum_counts.index, textinfo='label+percent'))
        fig.update_layout(
            legend_title_text="Вид Фоива",
            margin_l=0,
            margin_r=0,
            margin_t=20,
            margin_b=0)
        return fig

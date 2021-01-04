import seaborn as sns


def barplot(df, x, y, show_bar_annotation=False):
    '''
    INPUT 
        df - a dataframe
        x - string for column name to be plot on x axis
        y - string for column name to be plot on y axis
        show_bar_annotation - bool, dafault False, providing whether or not to show annotation on bars
        
    OUTPUT
        Displays a bar plot
    '''
    
    bar_plot = sns.barplot(y=y, x=x, data=df, palette='Reds_r')
    if show_bar_annotation:
        for p in bar_plot.patches:
            bar_plot.annotate(format(p.get_width(), '.2f'), (p.get_width() - 6, p.get_y() + p.get_height() / 2., ),
                              ha = 'center', va = 'center', xytext = (10, 0), textcoords = 'offset points')
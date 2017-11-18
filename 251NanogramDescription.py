import numpy as np

def hanjie_description(hanjie):

    # column description
    def nanogram_column(column):
        counter = 0
        column_labels = []

        for x in column:
            if x:
                counter += 1
            elif counter >= 1:
                column_labels.append(str(counter))
                counter = 0

        if counter >= 1 or column_labels == []:
            column_labels.append(str(counter))

        return column_labels

    print('Columns: ')
    for column in hanjie:
        column_description = nanogram_column(column)
        print(' '.join(column_description))

    print('Rows: ')
    for row in np.asarray(hanjie).T.tolist():
        row_description = nanogram_column(row)
        print(' '.join(row_description))

print(hanjie_description([[1,'','','',1],
                       ['',1,1,'',1],
                       [1,1,'',1,''],
                       ['','','','',''],
                       [1,'','','',1]]))
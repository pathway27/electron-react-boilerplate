
class WikipediaTable:
    def __init__(self, table_selector):
        self.table_selector = table_selector

    def run(self):
        quarter_rows = self.table_selector.css('tr')
        headers = [x.lower()
                    for x in quarter_rows.pop(0).css('th::text').getall()]

        rowspans = {}

        for game_row in quarter_rows:
            columns = game_row.css('td')
            columns_data = [
                ''.join(x.css('::text').getall()).strip() for x in columns]

            rowspans_columns = columns.css('td[rowspan]')
            if rowspans_columns:
                if len(rowspans.keys()) == 0:
                    for index, column in enumerate(rowspans_columns):
                        rowspans[headers[index]] = (
                            ''.join(column.css('::text').getall()).strip(),
                            int(column.attrib['rowspan'])
                        )
                else:
                    column = rowspans_columns[0]
                    rowspans[headers[1]] = (
                        ''.join(column.css('::text').getall()).strip(),
                        int(column.attrib['rowspan'])
                    )

            if len(columns_data) == 7:
                month = columns_data[0]
                day = columns_data[1]
            else:
                month = rowspans.get(headers[0], [None])[
                    0] or columns_data[0]
                day = rowspans.get(headers[1], [None])[
                    0] or columns_data[0]

            default_fields = {
                'month': month,
                'day': day
            }
            other_headers = headers[2:]

            # DEBUG
            # if day == 'FEBRUARY':
            #     import pdb
            #     pdb.set_trace()

            for header in rowspans.keys():
                value, count = rowspans[header]
                rowspans[header] = (value, count - 1)
            rowspans = {k: v for k, v in rowspans.items() if v[1] > 0}

            yield {**default_fields, **dict(zip(headers[-5:], columns_data[-5:]))}


    def run2(self):
        quarter_rows = self.table_selector.css('tr')
        headers = [x.lower()
                    for x in quarter_rows.pop(0).css('th::text').getall()]

        rowspans = {}

        for game_row in quarter_rows:
            columns = game_row.css('td')
            columns_data = [
                ''.join(x.css('::text').getall()).strip() for x in columns]

            rowspans_columns = columns.css('td[rowspan]')
            if rowspans_columns:
                if len(rowspans.keys()) == 0:
                    for index, column in enumerate(rowspans_columns):
                        rowspans[headers[index]] = (
                            ''.join(column.css('::text').getall()).strip(),
                            int(column.attrib['rowspan'])
                        )
                else:
                    column = rowspans_columns[0]
                    rowspans[headers[1]] = (
                        ''.join(column.css('::text').getall()).strip(),
                        int(column.attrib['rowspan'])
                    )

            if len(columns_data) == 7:
                month = columns_data[0]
                day = columns_data[1]
            else:
                month = rowspans.get(headers[0], [None])[
                    0] or columns_data[0]
                day = rowspans.get(headers[1], [None])[
                    0] or columns_data[0]

            default_fields = {
                'month': month,
                'day': day
            }
            other_headers = headers[2:]

            # DEBUG
            # if day == 'FEBRUARY':
            #     import pdb
            #     pdb.set_trace()

            for header in rowspans.keys():
                value, count = rowspans[header]
                rowspans[header] = (value, count - 1)
            rowspans = {k: v for k, v in rowspans.items() if v[1] > 0}

            yield {**default_fields, **dict(zip(headers[-5:], columns_data[-5:]))}

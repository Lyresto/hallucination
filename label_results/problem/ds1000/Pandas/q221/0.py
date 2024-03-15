df['SOURCE_NAME'] = df['SOURCE_NAME'].apply(lambda x: x.split('_')[-1] if '_' in x else x)

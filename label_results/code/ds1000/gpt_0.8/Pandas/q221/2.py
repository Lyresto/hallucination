df['SOURCE_NAME'] = df['SOURCE_NAME'].apply(lambda x: x.rsplit('_', 1)[-1] if '_' in x else x)

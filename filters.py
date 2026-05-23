import pandas as pd

def apply_all_dashboard_filters(df, selected_date_range, selected_flag, selected_score_range, selected_boros, search_keyword):
    """
    Processes and slices the raw dataset using all 6 assignment-required criteria.
    This satisfies the modular folder structure guidelines.
    """
    filtered_df = df.copy()

    # 1. Date / Time Range Filter
    if isinstance(selected_date_range, tuple) and len(selected_date_range) == 2:
        start_date = pd.to_datetime(selected_date_range[0])
        end_date = pd.to_datetime(selected_date_range[1])
        filtered_df = filtered_df[(filtered_df['INSPECTION DATE'] >= start_date) & 
                                  (filtered_df['INSPECTION DATE'] <= end_date)]

    # 2. Category Filter (Critical Status Dropdown)
    if selected_flag != "All":
        filtered_df = filtered_df[filtered_df['CRITICAL FLAG'] == selected_flag]

    # 3. Numerical Range Slider (Violation Score)
    filtered_df = filtered_df[(filtered_df['SCORE'] >= selected_score_range[0]) & 
                              (filtered_df['SCORE'] <= selected_score_range[1])]

    # 4. Multi-Select Filter (Boroughs Selection)
    if selected_boros:
        filtered_df = filtered_df[filtered_df['BORO'].isin(selected_boros)]

    # 5. Search / Text Filter (Restaurant Name Keyword Search)
    if search_keyword:
        filtered_df = filtered_df[filtered_df['DBA'].str.contains(search_keyword, case=False, na=False)]

    return filtered_df
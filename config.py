CALL_DATA_PTH = "data/call_data.csv"
MSG_DATA_PTH = "data/message_data.csv"
SEARCH_DATA_PTH = "data/search_data.csv"
SIGNUP_DATA_PTH = "data/signup_data.csv"

USER_FEATURES_ENG_DATA_PTH = "data/processed/user_features_eng.csv"
USER_FEATURES_DATA_PTH = "data/processed/user_features.pkl"

USER_FEATURES = ['total_calls',
       'total_messages', 'total_searches', 
       'call_frequency', 'days_signup_to_first_call', 'call_span_days',
       'message_frequency',
       'days_signup_to_first_message', 'message_span_days', 
       'search_frequency', 'days_signup_to_first_search',
       'search_span_days', 'call_rate_per_day', 'call_message_per_day',
       'call_searches_per_day', 'total_activity',
       'search_to_communication_ratio', 'immediate_activity',
       'activity_concentration',
       # 'search_interval_mean_sec', 'search_interval_min_sec',
       # 'search_interval_std_sec', 'call_interval_mean_sec',
       # 'call_interval_min_sec', 'call_interval_std_sec',
       # 'message_interval_mean_sec', 'message_interval_min_sec',
       # 'message_interval_std_sec'
       ]

MODEL_ISOLATION_FOREST_PTH = "models/isolation_forest_preds.csv"
AUTOENCODER_ISOLATION_FOREST_PTH = "models/autoencoder_preds.csv"

FINAL_RESULTS_PTH = "final_results.csv"
### Feature Importance 視覺化執行流程

1. 下載此份 code 到本機 (或是從 git clone 到 remote server)

`git clone https://github.com/YoEugene/epa2020_feature_importance.git`

2. cd 進入此資料夾

3. 安裝所有相關套件

`python3 -m pip install -r requirements.txt`

4. (Optional) 若安裝過程發生錯誤，可能是 pip 套件要進行更新。若無發生錯誤可跳過此步。

`python3 -m pip install --upgrade pip`

5. 以 python3 運行這份 code

`python3 feature_imp_visualization.py`

6. 若成功，會看到以下字樣

```console
Dash is running on http://0.0.0.0:8080/

 Warning: This is a development server. Do not use app.run_server
 in production, use a production WSGI server like gunicorn instead.

 * Serving Flask app "feature_imp_visualizarion" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)
```

7. 打開瀏覽器，輸入以上網址，即可進入視覺化圖表

8. (Optional) 打開 feature_imp_visualization.py，修改 `feature_ind` 變數，即可切換不同空汙項

`0 -> PM25, 1 -> PM10. 2 -> O3, 3 -> NO2`
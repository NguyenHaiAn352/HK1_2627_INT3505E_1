1. curl.exe 'http://127.0.0.1:5000/orders?status=paid'
   ![Filtering](lab3_1.png)

2. curl.exe 'http://127.0.0.1:5000/orders?limit=5'
   ![Limit](lab3_2.png)

3. curl.exe 'http://127.0.0.1:5000/orders?fields=id&limit=5'
   ![Sparse_Fieldset](lab3_3.png)

4. curl.exe 'http://127.0.0.1:5000/orders?cursor=tu' || curl.exe 'http://127.0.0.1:5000/orders?cursor=11'
   ![Errors](lab3_4.png)

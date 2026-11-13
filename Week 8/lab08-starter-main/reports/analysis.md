1. Trong 3 kịch bản, kịch bản nào có p95 cao nhất? Vì sao?
   Trong 3 kịch bản, kịch bản C có 95%ile cao nhất. Vì kịch bản C là spike test, với rate là load 50 người trong một giây, hệ thống sẽ có thể không xử lý kịp users trước khi các users sau truy cập, dẫn đến số lượng người nằm sau 95%ile cao hơn hẳn so với hai kịch bản trước.
2. Có endpoint nào fail rate tăng theo số user? Đoán nguyên nhân dựa trên code.
   Có endpoint "GET /books?year=2020" là fail rate tăng theo số user, vì ta đã cài base failrate 1% cho method. Càng nhiều users thì khả năng kích hoạt fail rate sẽ càng tăng cao.
3. Nếu prod cần SLO p95 < 300ms, kịch bản nào đạt? Đề xuất baseline cho CI gate.
   Cả ba kịch bản đều đạt SLO 95%ile <300ms (KB A avg p95 = 20ms, KB B avg p95 = 22ms, KB C avg p95 = 100ms). Kịch bản C phù hợp cho CI gate vì nó phản ánh khá thực tế về số lượng người dùng truy cập trên 1 giây.

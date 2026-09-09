# import library dulu
import cv2
from ultralytics import YOLO

# fungsi deteksi objek
def deteksiObjek(frame):
    hasil=model(frame)
    daftarObjek=[]
    for i in hasil:
        for kotak in i.boxes:
            namaObjek=int(kotak.cls[0])
            tingkatPercaya=kotak.conf[0].item()

            if tingkatPercaya>0.5:
                label=model.names[namaObjek] # memberikan label pada objek 
                daftarObjek.append(label)

                # menggambar bounding box
                x1,y1,x2,y2=map(int, kotak.xyxy[0])
                cv2.rectangle(frame, (x1,y1), (x2,y2), (0,255,0), 2)
                # menulis nama objek dan tingkat kepercayaan
                teks= f"{model.names[namaObjek]} {tingkatPercaya:.2f}"
                cv2.putText(frame, teks, (x1,y1-10), cv2.FONT_HERSHEY_COMPLEX, 0.6, (0,0,255),2)
    return frame, daftarObjek


# aktifkan model yolov8n
model= YOLO("yolov8n.pt")

# membuka webcam
cap=cv2.VideoCapture(0)

while True: # mengambil frame dari webcam
    ret, frame= cap.read()
    if not ret:
        break
    frame, daftarObjek= deteksiObjek(frame) # untuk mendeteksi objek
    if deteksiObjek:
        print("Objek Terdektesi ", daftarObjek)
    # menampilkan hasil/menampilkan keluaran
    cv2.namedWindow("YOLOv8 Detection", cv2.WINDOW_NORMAL) # tampilan di layar 
    cv2.resizeWindow("YOLOv8 Detection", 1280,720) # mempebedar tampilan di layar
    cv2.imshow("YOLOv8 Detection", frame)
    if cv2.waitKey(1) & 0xFF==ord("s"): # jika tekan s di keyboard maka akan berhenti
        break

# menutup webcam
cap.release()
cv2.destroyAllWindows()

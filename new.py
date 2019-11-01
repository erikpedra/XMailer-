# -*- coding: utf-8 -*-
__author__ = 'Fu'

import socket
import ssl
import base64
import time
import os
import random


class SendMail:
    __username = ''
    __password = ''
    __recipient = ''
    msg = b'\r\n'
    endmsg = b'\r\n.\r\n'
    mailserver = ('smtp.qq.com', 465) # Server SMTP !
    heloCommand = b'HELO qq.com\r\n'
    loginCommand = b'AUTH login\r\n'
    dataCommand = b'DATA\r\n'
    quitCommand = b'QUIT\r\n'
    msgsubject = b'Subject: Test E-mail\r\n'
    msgtype = b"Content-Type: multipart/mixed;boundary='BOUNDARY'\r\n\r\n"
    msgboundary = b'--BOUNDARY\r\n'
    msgmailer = b'X-Mailer:Fu\'s mailer\r\n'
    msgMIMI = b'MIME-Version:1.0\r\n'
    msgfileType = b"Content-type:application/octet-stream;charset=utf-8\r\n"
    msgfilename = b"Content-Disposition: attachment; filename=''\r\n"
    msgimgtype = b"Content-type:image/gif;\r\n"
    msgimgname = b"Content-Disposition: attachment; filename=''\r\n"
    msgtexthtmltype = b'Content-Type:text/html;\r\n'
    msgimgId = b'Content-ID:<test>\r\n'
    msgimgscr = b'<img src="cid:test">'
    mailcontent = ''
    __clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def login(self):
        """
        Masukkan nama pengguna dan kode otorisasi untuk masuk ke kotak surat QQ.
        """
        try:
            #print("Mengirim permintaan login……")
            time.sleep(1)
            self.__sslclientSocket.send(self.loginCommand)
            recv2 = self.__sslclientSocket.recv(1024).decode('utf-8')
            if recv2[:3] != '334':
                #print('Permintaan masuk gagal dikirim：334 reply not received from server.')
                time.sleep(2)
                #print('Coba lagi……')
                self.login()
            #print("Permintaan login berhasil dikirim……")
            self.__username = 'm15730702970@163.com'  # input("Silakan masukkan nama pengguna：")
            self.__password = 'zjf123456789'  ##input("Silakan masukkan kata sandi：")
            #print("Masuk……")
            time.sleep(1)
            username = b'%s\r\n' % base64.b64encode(self.__username.encode('GBK'))
            self.__sslclientSocket.send(username)
            recv = self.__sslclientSocket.recv(1024).decode('utf-8')
            password = b'%s\r\n' % base64.b64encode(self.__password.encode('GBK'))
            self.__sslclientSocket.send(password)
            recv = self.__sslclientSocket.recv(1024).decode('GBK')
            if recv[:3] != '235':
                #print('Gagal masuk: akun atau kata sandi salah, harap gunakan kode otorisasi untuk masuk.. 235 reply not received from server.', recv)
                time.sleep(2)
                #print('Coba lagi……')
                self.login()
            #print("Login berhasil")
            time.sleep(1)
        except Exception as e:
            print(e)

    def socketconnet(self):
        """
        Gunakan soket soket untuk terhubung ke server kotak surat qq dan mengatur otentikasi ssl
        """
        #print("Menghubungkan ke server……")
        time.sleep(1)
        self.__sslclientSocket = ssl.wrap_socket(self.__clientSocket, cert_reqs=ssl.CERT_NONE,
        ssl_version=ssl.PROTOCOL_SSLv23)
        self.__sslclientSocket.connect(self.mailserver)
        recv = self.__sslclientSocket.recv(1024).decode('utf-8')
        if recv[:3] != '220':
            #print('Koneksi server gagal：220 reply not received from server.')
            time.sleep(2)
            #print('Coba lagi……')
            self.socketconnet()
        #print("Berhasil terhubung ke server……")
        time.sleep(1)
        #print("Meminta respons server……")
        time.sleep(1)
        self.__sslclientSocket.send(self.heloCommand)
        recv1 = self.__sslclientSocket.recv(1024).decode('utf-8')
        if recv1[:3] != '250':
            #print('Respons server gagal：250 replay not received from server')
            time.sleep(2)
            #print('Coba lagi……')
            self.socketconnet()
        #print("Berhasil meminta respons server……")
        time.sleep(1)

    def sender(self):
        mailsenderCommand = b'MAIL FROM:<%s>\r\n' % self.__username.encode('utf-8')
        self.__sslclientSocket.send(mailsenderCommand)

    def recipient(self):
        self.__recipient = input("Silakan masukkan alamat email penerima：")
        time.sleep(1)
        mailrecipientCommand = b'RCPT TO:<%s>\r\n' % self.__recipient.encode('utf-8')
        self.__sslclientSocket.send(mailrecipientCommand)
        recv = self.__sslclientSocket.recv(1024).decode('utf-8')
        if recv[:3] != '250':
            #print("Kesalahan kotak surat penerima:250 replay not received from server")
            time.sleep(1)
            self.recipient()

    def senddata(self):
        self.__sslclientSocket.send(self.dataCommand)
        recv = self.__sslclientSocket.recv(1024).decode('utf-8')
        if recv[:3] != '354':
            time.sleep(1)
            self.senddata()

    def sendsubject(self):
        subject = input("Silakan masukkan subjek email：")
        time.sleep(1)
        self.msgsubject = b'Subject: %s\r\n' % subject.encode('utf-8')
        self.__sslclientSocket.send(self.msgsubject)
        self.__sslclientSocket.send(self.msgmailer)
        self.__sslclientSocket.send(self.msgtype)
        self.__sslclientSocket.send(b'Content-Transfer-Encoding:7bit\r\n\r\n')

    def writemail(self):
        self.__sslclientSocket.send(b'\r\n\r\n' + self.msgboundary)
        self.__sslclientSocket.send(b'Content-Type: text/html;charset=utf-8\r\n')
        self.__sslclientSocket.send(b'Content-Transfer-Encoding:7bit\r\n\r\n')
        self.mailcontent = input("Silakan masukkan isi email：\n")
        time.sleep(1)
        self.__sslclientSocket.sendall(b'%s\r\n' % self.mailcontent.encode('utf-8'))

    def addfile(self):
        filepath = input("Please enter the file path：")
        time.sleep(1)
        # filepath=filepath.replace('\\','/')
        if os.path.isfile(filepath):
            filename = os.path.basename(filepath)
            # #print(filename)
            time.sleep(0.1)
            self.__sslclientSocket.send(b'\r\n\r\n' + self.msgboundary)
            self.__sslclientSocket.send(self.msgfileType)
            self.msgfilename = b"Content-Disposition: attachment; filename='%s'\r\n" % filename.encode('utf-8')
            self.__sslclientSocket.send(self.msgfilename)
            # #print(self.msgfilename)
            self.__sslclientSocket.send(b'Content-Transfer-Encoding:base64\r\n\r\n')
            self.__sslclientSocket.send(self.msg)
            # #print(1)
            time.sleep(0.1)
            fb = open(filepath, 'rb')
            while True:
                filedata = fb.read(1024)
                # #print(filedata)
                if not filedata:
                    break
                self.__sslclientSocket.send(base64.b64encode(filedata))
                time.sleep(1)
            fb.close()
            # #print(2)
            time.sleep(0.1)

    def addimg(self):
        self.mailcontent = input("Please enter the body of the email：")
        time.sleep(1)
        filepath = input("Please enter the image path：")
        time.sleep(1)
        # filepath = filepath.replace('\\', '/')
        if os.path.isfile(filepath):
            # #print(1)
            time.sleep(0.1)
            filename = os.path.basename(filepath)
            randomid = filename.split('.')[1] + str(random.randint(1000, 9999))
            # #print(randomid)
            time.sleep(0.1)
            self.msgimgId = b'Content-ID:%s\r\n' % randomid.encode('utf-8')
            self.__sslclientSocket.send(b'\r\n\r\n' + self.msgboundary)
            self.__sslclientSocket.send(self.msgimgtype)
            self.__sslclientSocket.send(self.msgimgId)
            self.msgimgname = b"Content-Disposition: attachment; filename='%s'\r\n" % filename.encode('utf-8')
            self.__sslclientSocket.send(self.msgfilename)
            # #print(self.msgimgId)
            time.sleep(0.1)
            self.__sslclientSocket.send(b'Content-Transfer-Encoding:base64\r\n\r\n')
            self.__sslclientSocket.send(self.msg)
            fb = open(filepath, 'rb')
            while True:
                filedata = fb.read(1024)
                # #print(filedata)
                if not filedata:
                    break
                self.__sslclientSocket.send(base64.b64encode(filedata))
                time.sleep(0.1)
            fb.close()
            # #print(1)
            time.sleep(0.1)
            self.__sslclientSocket.send(b'\r\n\r\n' + self.msgboundary)
            self.__sslclientSocket.send(self.msgtexthtmltype)
            self.__sslclientSocket.send(b'Content-Transfer-Encoding:8bit\r\n\r\n')
            msgimgscr = b'<img src="cid:%s">' % randomid.encode('utf-8')
            # #print(1)
            time.sleep(0.1)
            self.__sslclientSocket.send(msgimgscr)
            # #print(msgimgscr)
            time.sleep(0.1)
            self.__sslclientSocket.sendall(b'%s' % self.mailcontent.encode('utf-8'))
            # #print(msgimgscr)
            time.sleep(0.1)

    def sendmail(self):
        # self.addimg()
        # #print(1)
        # time.sleep(1)
        # self.addfile()
        # #print(2)
        # self.__sslclientSocket.send(self.endmsg)
        bool_addimg = input("Whether to add a picture <Y/N>:")
        bool_addfile = input("Whether to add attachments <Y/N>:")
        if bool_addimg.lower() == 'y':
            if bool_addfile.lower() == 'y':
                self.addimg()
                #print(1)
                self.addfile()
                #print(2)
                self.__sslclientSocket.send(self.endmsg)
            else:
                self.addimg()
                self.__sslclientSocket.send(self.endmsg)
        else:
            if bool_addfile.lower() == 'y':
                self.writemail()
                self.addfile()
                self.__sslclientSocket.send(self.endmsg)
            else:
                self.writemail()
                self.__sslclientSocket.send(self.endmsg)

    def quitconnect(self):
        self.__sslclientSocket.send(self.quitCommand)


if __name__ == '__main__':
    try:
        sendmail = SendMail()
        sendmail.socketconnet()
        sendmail.login()
        sendmail.sender()
        sendmail.recipient()
        sendmail.senddata()
        sendmail.sendsubject()
        sendmail.sendmail()
        time.sleep(1)
        #print("Sent successfully！")
        sendmail.quitconnect()
    except Exception:
        print(Exception)
    finally:
        exit(0)

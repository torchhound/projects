package simpleserver;

import java.net.*;
import java.io.*;

public class simpleServer extends Thread{
	private ServerSocket serverSocket;
	public simpleServer(int port) throws IOException{
		serverSocket = new ServerSocket(port);
		serverSocket.setSoTimeout(500);
	}
	public void run(){
		while(true){
			try{
				Socket server = serverSocket.accept();
				System.out.println("Client at: " + server.getRemoteSocketAddress());
				DataInputStream inbound = new DataInputStream(server.getInputStream());
        System.out.println(inbound.readUTF());
				DataOutputStream outbound = new DataOutputStream(server.getOutputStream());
				outbound.writeUTF(server.getLocalSocketAddress().toString());
				server.close();
			}catch(SocketTimeoutException s){
				s.printStackTrace();
				break;
			}catch(IOException e){
				e.printStackTrace();
				break;
			}
		}
	}
	public static void main(String[] args){
		int port = Integer.parseInt(args[0]);
		try{
			Thread t = new simpleServer(port);
			t.start();
		}catch(IOException e){
			e.printStackTrace();
		}
	}
}

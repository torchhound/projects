package simpleclient;

import java.net.*;
import java.io.*;

public class simpleClient{
	public static void main(String[] args){
		String server = args[0];
		int port = Integer.parseInt(args[1]);
		try {
			Socket client = new Socket(server, port);
			System.out.println("Connection made: " + client.getRemoteSocketAddress());
			OutputStream toServer = client.getOutputStream();
			DataOutputStream outbound = new DataOutputStream(toServer);
			outbound.writeUTF(client.getLocalSocketAddress().toString());
			InputStream fromServer = client.getInputStream();
			DataInputStream inbound = new DataInputStream(fromServer);
			System.out.println(inbound.readUTF());
			client.close();
		}catch(IOException e){
			e.printStackTrace();
		}
	}
}

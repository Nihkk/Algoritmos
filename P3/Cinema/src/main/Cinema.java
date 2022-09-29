package main;

import java.util.ArrayList;

public class Cinema {

	private ArrayList<Cliente> clientes;
	
	public Cinema() {
		this.clientes = new ArrayList<Cliente>();
	}
	
	public void adicionarCliente(Cliente c) {
		for(Cliente a : clientes) {
			if(!a.equals(c)) {
				clientes.add(c);
			}
		}
	}
	
	public void removerCliente(Cliente c) {
		for(Cliente a : clientes) {
			if(a.equals(c)) {
				clientes.remove(c);
			}
		}
	}
}




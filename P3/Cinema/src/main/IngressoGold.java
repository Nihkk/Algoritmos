package main;

public class IngressoGold extends IngressoComum {
	
	
	public IngressoGold(String filme, String data, int sala, String horario, double valor) {
		super(filme, data, sala, horario, valor);
		// TODO Auto-generated constructor stub
	}

	public double calcularValor(double valor) {
		return valor - (valor * 0.08);
	}
	
}

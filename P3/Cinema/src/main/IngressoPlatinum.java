package main;

public class IngressoPlatinum extends IngressoComum{

	public IngressoPlatinum(String filme, String data, int sala, String horario, double valor) {
		super(filme, data, sala, horario, valor);
		// TODO Auto-generated constructor stub
	}

	public double calcularValor(double valor) {
		return valor - (valor * 0.12);
	}
	
	
}

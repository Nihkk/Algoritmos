package main;

public class IngressoComum {
	
	private String data;
	private String filme;
	private int sala;
	private String horario;
	private double valor;
	
	public IngressoComum(String filme, String data, int sala, String horario, double valor) {
		this.filme = filme;
		this.data = data;
		this.sala = sala;
		this.horario = horario;
		this.valor = valor;
	}
	
	public String getData() {
		return data;
	}
	public void setData(String data) {
		this.data = data;
	}
	public String getFilme() {
		return filme;
	}
	public void setFilme(String filme) {
		this.filme = filme;
	}
	public int getSala() {
		return sala;
	}
	public void setSala(int sala) {
		this.sala = sala;
	}
	public String getHorario() {
		return horario;
	}
	public void setHorario(String horario) {
		this.horario = horario;
	}
	public double getValor() {
		return valor;
	}
	public void setValor(double valor) {
		this.valor = valor;
	}
	
	@Override
	public String toString() {
		return "IngressoComum [data=" + data + ", filme=" + filme + ", sala=" + sala + ", horario=" + horario
				+ ", valor=" + valor + "]";
	}

}

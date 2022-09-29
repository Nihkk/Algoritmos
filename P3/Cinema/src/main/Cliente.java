package main;

public class Cliente {
	
	private String nome;
	private int cpf;
	private int cartao;
	private int ingressos;
	
	public Cliente(String nome, int cpf, int cartao, int ingressos) {
		this.nome = nome;
		this.cpf = cpf;
		this.cartao = cartao;
		this.ingressos = ingressos;
	}
	
	@Override
	public boolean equals(Object obj) {
		boolean result = false;
		if((obj != null) && (obj instanceof Cliente)) {
			Cliente c = (Cliente) obj;
			
			if(this.cpf == c.cpf) {
				result = true;
			}
		}
		return result;
	}

	public String getNome() {
		return nome;
	}

	public void setNome(String nome) {
		this.nome = nome;
	}

	public int getCpf() {
		return cpf;
	}

	public void setCpf(int cpf) {
		this.cpf = cpf;
	}

	public int getCartao() {
		return cartao;
	}

	public void setCartao(int cartao) {
		this.cartao = cartao;
	}

	public int getIngressos() {
		return ingressos;
	}

	public void setIngressos(int ingressos) {
		this.ingressos = ingressos;
	}
	
	public void comprarIngressos(int quant) {
		this.ingressos = this.ingressos + quant;
	}

	@Override
	public String toString() {
		return "Cliente [nome=" + nome + ", cpf=" + cpf + ", cartao=" + cartao + ", ingressos=" + ingressos + "]";
	}

	
}

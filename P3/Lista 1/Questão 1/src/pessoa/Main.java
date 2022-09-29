package pessoa;

public class Main {

	public static void main(String[] args) {
		
		Pessoa p = new Pessoa();
		
		p.setNome("Luan");
		p.setId(1);
		p.setIdade(19);
		
		Pessoa p2 = new Pessoa("Giovana", 18, 2);
		
		System.out.println(p);
		System.out.println(p2);
	}
}

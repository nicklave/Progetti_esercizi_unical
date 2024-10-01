package contratticalciatori;

public class Calciatore 
{	private String nome;
	private String squadraAttuale;
	
	public Calciatore(String nome, String squadraAttuale) 
	{	this.nome = nome;
		this.squadraAttuale = squadraAttuale;
	}

	public String getNome() 
	{	return nome;
	}

	public String getSquadraAttuale() 
	{	return squadraAttuale;
	}
	
	public boolean equals(Object o)
	{	if(o == null)
			return false;
		if(o == this)
			return true;
		if(!(o instanceof Calciatore))
			return false;
		Calciatore c = (Calciatore)o;
		return nome.equals(c.nome);
	}
	
	public String toString()
	{	return "Calciatore "+nome+", squadra attuale "+squadraAttuale;
	}
}

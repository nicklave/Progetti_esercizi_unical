package conticorrenti;

public class Movimento //LA CLASSE GENERA OGGETTI IMMUTABILI
{	private String tipo;
	private float valore;
	
	public Movimento(String tipo, float valore)
	{	this.tipo = tipo;
		this.valore = valore;		
	}
	
	public String getTipo()
	{	return tipo;		
	}
	
	public float getValore()
	{	return valore;		
	}
	
	public String toString()
	{	return "Movimento di tipo "+tipo+" e valore "+valore;		
	}
	
	public boolean equals(Object o)
	{	if(o == null)
			return false;
		if(o == this)
			return true;
		if(!(o instanceof Movimento))
			return false;
		Movimento m = (Movimento)o;
		return tipo.equals(m.tipo) && valore == m.valore;
	}
}

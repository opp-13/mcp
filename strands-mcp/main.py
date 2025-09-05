import httpx
from bs4 import BeautifulSoup
from fastmcp import FastMCP

mcp = FastMCP("Strands Code Generator")

@mcp.tool()
def crawl_strands_info(query: str) -> str:
    """Crawl strands information from internet"""
    try:
        search_url = f"https://www.google.com/search?q={query}+strands"
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        
        with httpx.Client() as client:
            response = client.get(search_url, headers=headers, timeout=10)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            snippets = []
            for div in soup.find_all('div', class_=['BNeawe', 'VwiC3b']):
                text = div.get_text().strip()
                if text and 'strand' in text.lower():
                    snippets.append(text)
            
            return "\n".join(snippets[:3]) if snippets else "No strands info found"
    except Exception as e:
        return f"Error: {str(e)}"

@mcp.tool()
def generate_strands_code(info: str, language: str = "python") -> str:
    """Generate code based on strands information"""
    if language == "python":
        return f'''class Strand:
    def __init__(self, data):
        self.data = data
    
    def process(self):
        # Based on: {info[:50]}...
        return self.data.split()

strand = Strand("{info[:30]}...")'''
    else:
        return f"// {language} code for: {info[:50]}..."

@mcp.tool()
def auto_strands_workflow(query: str, language: str = "python") -> str:
    """Complete workflow: crawl and generate code"""
    info = crawl_strands_info(query)
    code = generate_strands_code(info, language)
    return f"INFO:\n{info}\n\nCODE:\n{code}"

if __name__ == "__main__":
    mcp.run()

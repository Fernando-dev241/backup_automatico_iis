import os
import shutil
from datetime import datetime

class ServicoBackup:
    """
    Classe que aplica conceitos de Orientação a Objetos (POO) 
    para gerenciar a automação de infraestrutura do servidor.
    """
    def __init__(self, pasta_origem, pasta_destino):
        # Atributos encapsulados do objeto
        self.origem = pasta_origem
        self.destino = pasta_destino

    def verificar_diretorios(self):
        """Verifica se a origem existe e prepara o destino."""
        if not os.path.exists(self.origem):
            print(f"[-] Erro Algorítmico: Pasta de origem '{self.origem}' não encontrada.")
            return False
        
        if not os.path.exists(self.destino):
            os.makedirs(self.destino)
            print(f"[+] Infraestrutura: Pasta de destino '{self.destino}' criada com sucesso.")
        return True

    def realizar_backup(self):
        """Executa a lógica algorítmica de compactação e cópia de segurança."""
        if not self.verificar_diretorios():
            return

        # Gerando timestamp para garantir arquivos únicos (Escalabilidade)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        nome_arquivo = f"backup_expo_tech_{timestamp}"
        caminho_final = os.path.join(self.destino, nome_arquivo)

        try:
            # Algoritmo de compactação em formato ZIP
            shutil.make_archive(caminho_final, 'zip', self.origem)
            print(f"[SUCESSO] Automação Concluída! Arquivo gerado: {nome_arquivo}.zip")
            self._simular_upload_nuvem(nome_arquivo) # Integração complementar em nuvem
        except Exception as e:
            print(f"[-] Falha na execução da rotina: {e}")

    def _simular_upload_nuvem(self, nome_arquivo):
        """Simula ou aponta para uma solução de Cloud Computing."""
        print(f"[CLOUD] Sincronizando '{nome_arquivo}.zip' com o repositório seguro em nuvem AWS/Azure...")
        print("[STATUS] Nuvem atualizada e redundância ativada.")


# Bloco de execução principal (Lógica de Inicialização)
if __name__ == "__main__":
    # Caminho do site no IIS (Origem) e local seguro na partição do SSD (Destino)
    DIRETORIO_SITE = r"C:\inetpub\wwwroot"
    DIRETORIO_BACKUP = r"C:\Backups_ExpoTech2026"

    # Instanciação do Objeto (POO)
    executor = ServicoBackup(DIRETORIO_SITE, DIRETORIO_BACKUP)
    
    # Chamada do método de automação
    executor.realizar_backup()
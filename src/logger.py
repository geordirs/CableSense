import logging
import os

def setup_logger():
    os.makedirs('logs', exist_ok=True)

    # Audit Logger (for security events)
    audit_logger = logging.getLogger('audit')
    audit_logger.setLevel(logging.INFO)
    audit_handler = logging.FileHandler('logs/audit.log')
    audit_handler.setFormatter(logging.Formatter('%(asctime)s - AUDIT - %(message)s'))
    audit_logger.addHandler(audit_handler)

    # System Logger
    system_logger = logging.getLogger('system')
    system_logger.setLevel(logging.INFO)
    system_handler = logging.FileHandler('logs/system.log')
    system_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
    system_logger.addHandler(system_handler)

    return system_logger, audit_logger

system_log, audit_log = setup_logger()

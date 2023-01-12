from datetime import timedelta
from typing import Dict, Any

from celery import Celery

BROKER_URL = ""

config = {
    "broker_url": BROKER_URL,
    "task_ignore_result": True,
    "worker_concurrency": 1,
    "worker_disable_rate_limits": True,
    "worker_hijack_root_logger": True
}
celery = Celery("tasks", broker=config.pop("broker_url"))
celery.conf.update(**config)

# task_queues must be defined in consumer
celery.conf.task_queues = {
    f'{project_slug}:beat_queue': {
        'queue_arguments': {'x-queue-mode': 'lazy'}
    },
    f'{project_slug}:subscription_queue': {
        'queue_arguments': {'x-queue-mode': 'lazy'}
    },
    f'{project_slug}:payment_queue': {
        'queue_arguments': {'x-queue-mode': 'lazy'}
    },
    f'{project_slug}:coupon_queue': {
        'queue_arguments': {'x-queue-mode': 'lazy'}
    }
}

# task_routes of tasks that called from a worker must be defined in consumer
celery.conf.task_routes = [
    {'src.tasks.beats.*': {'queue': f'{project_slug}:beat_queue'}},
    {'src.tasks.subscription.tasks.*': {'queue': f'{project_slug}:subscription_queue'}},
    {'src.tasks.coupon.tasks.*': {'queue': f'{project_slug}:coupon_queue'}},
    {'src.tasks.invoice.tasks.*': {'queue': f'{project_slug}:payment_queue'}}
]


def __prepare_beat_schedule() -> Dict[str, Any]:
    schedule: Dict[str, Any] = {
        'beat_update_subscriptions': {
            'task': 'src.tasks.beats.beat_update_subscriptions',
            'schedule': timedelta(minutes=configuration.BEAT_UPDATE_SUBSCRIPTIONS_INTERVAL),
            'options': {'expires': configuration.EXPIRE_TIME_OF_TASKS}
        },
        'beat_charge_invoices': {
            'task': 'src.tasks.beats.beat_charge_invoices',
            'schedule': timedelta(minutes=configuration.BEAT_CHARGE_INVOICES_INTERVAL),
            'options': {'expires': configuration.EXPIRE_TIME_OF_TASKS}
        },
        'beat_check_coupons': {
            'task': 'src.tasks.beats.beat_check_coupons',
            'schedule': timedelta(minutes=configuration.BEAT_CHECK_COUPONS_INTERVAL),
            'options': {'expires': configuration.EXPIRE_TIME_OF_TASKS}
        },
        'beat_finalize_invoices': {
            'task': 'src.tasks.beats.beat_finalize_invoices',
            'schedule': timedelta(minutes=configuration.BEAT_FINALIZE_INVOICES_INTERVAL),
            'options': {'expires': configuration.EXPIRE_TIME_OF_TASKS}
        },
        'beat_update_invoices': {
            'task': 'src.tasks.beats.beat_update_invoice_amounts',
            'schedule': timedelta(minutes=configuration.BEAT_UPDATE_INVOICES_INTERVAL),
            'options': {'expires': configuration.EXPIRE_TIME_OF_TASKS}
        }
    }
    return schedule


celery.conf.beat_schedule = __prepare_beat_schedule()

import src.tasks  # NOQA

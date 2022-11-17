import docker
import logging

client = docker.DockerClient(base_url='unix://var/run/docker.sock')
lowLevelClient = docker.APIClient(base_url='unix://var/run/docker.sock')
logger = logging.getLogger(__name__)


def login(registry, username, password):
    try:
        result = client.login(registry=registry, username=username, password=password)
        logger.info(result)
        return result
    except Exception as e:
        logger.error(e)
        raise e


def image_pull(repo, tag):
    logger.info("[Pulling image] " + repo)
    try:
        image = client.images.pull(repository=repo, tag=tag)
        logger.info("[Pulled image] " + image.id)
        return image
    except Exception as e:
        logger.error(e)
        raise e


def image_remove(image_url):
    logger.info("[Removing image] " + image_url)
    try:
        res = client.images.remove(image_url)
        logger.info("[Removed image] " + image_url)
        return res
    except Exception as e:
        logger.error(e)
        raise e


def image_list():
    try:
        return client.images.list()
    except Exception as e:
        logger.error(e)
        raise e


def image_inspect(image_url):
    try:
        return lowLevelClient.inspect_image(image_url)
    except Exception as e:
        logger.error(e)
        raise e


def container_create(name, image_url, env={}, ports={}):
    """Create a container without starting it. Similar to docker create."""

    logger.info("[Container create]: name: %s, image:%s, env: %s, ports: %s ", name, image_url, env, ports)
    try:
        container = client.containers.create(image=image_url,
                                             name=name,
                                            #  environment=env,
                                             ports=ports,
                                             labels={"purpose": "dev"})
        logger.info("[Container created]: name: %s, image:%s, id: %s", name, image_url, container.id)
        return container
    except Exception as e:
        logger.error(e)
        raise e


def container_list():
    """List containers. Similar to the docker ps command."""
    try:
        return client.containers.list(all=True, filters={"label": "purpose=dev"})
        # return client.containers.list(all=True)
    except Exception as e:
        logger.error(e)
        raise e


def container_get(id):
    try:
        return client.containers.get(id)
    except Exception as e:
        logger.error(e)
        raise e


def container_remove(id):
    try:
        return client.containers.get(id).remove()
    except Exception as e:
        logger.error(e)
        raise e


def container_start(id):
    return client.containers.get(id).start()


def container_stop(id):
    return client.containers.get(id).stop()


def container_kill(id):
    return client.containers.get(id).kill()


def container_restart(id):
    return client.containers.get(id).restart()


def container_pause(id):
    return client.containers.get(id).pause()


def container_resume(id):
    return client.containers.get(id).unpause()


def container_logs(id, lines=100):
    return client.containers.get(id).logs(tail=lines, timestamps=True)

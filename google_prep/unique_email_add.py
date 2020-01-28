class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        final_list = set()
        for email in emails:
            local_name, domain_name = email.split("@")
            processed_local_name = local_name.split("+")[0].replace(".", "")
            final_list.add(processed_local_name + "@" + domain_name)
        return len(final_list)

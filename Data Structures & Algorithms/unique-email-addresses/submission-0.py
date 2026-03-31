class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        h = set()
        for mail in emails:
            local, domain = mail.split("@")
            local = local.split("+")[0]
            local = local.replace(".", '')
            h.add((local, domain))
            

        return len(h)